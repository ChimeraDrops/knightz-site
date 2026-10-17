#!/usr/bin/env python3
"""Post new devlog entries to Discord.

Compares posts/index.json at BEFORE_SHA with the current checkout and sends one
Discord embed per new slug to the webhook in DISCORD_WEBHOOK_URL.

Env:
  DISCORD_WEBHOOK_URL  required, Discord channel webhook URL (repo secret)
  BEFORE_SHA           commit before the push; empty or all zeros posts nothing
  FORCE_SLUG           optional, post this slug regardless of diff (manual test)
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

SITE = "https://chimeradrops.github.io/knightz-site"
INDEX = "posts/index.json"
COLOR = 0xC9A227


def load_index(ref=None):
    if ref:
        try:
            raw = subprocess.check_output(["git", "show", f"{ref}:{INDEX}"], text=True)
        except subprocess.CalledProcessError:
            return []
    else:
        with open(INDEX, encoding="utf-8") as f:
            raw = f.read()
    return json.loads(raw)


def first_image(slug):
    path = f"posts/{slug}.md"
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        m = re.search(r"!\[[^\]]*\]\(([^)\s]+)\)", f.read())
    if not m:
        return None
    src = m.group(1)
    return src if src.startswith("http") else f"{SITE}/{src.lstrip('./')}"


def send(webhook, post):
    url = f"{SITE}/post.html?p={post['slug']}"
    embed = {
        "title": post["title"][:256],
        "url": url,
        "description": post.get("summary", "")[:4000],
        "color": COLOR,
        "footer": {"text": f"KSUIE_Gaming | {post.get('date', '')}"},
    }
    tags = post.get("tags") or []
    if tags:
        embed["fields"] = [{"name": "Tags", "value": ", ".join(tags)[:1024], "inline": False}]
    img = first_image(post["slug"])
    if img:
        embed["image"] = {"url": img}
    body = json.dumps({
        "username": "KnightZ Dev Log",
        "content": "New dev log is up.",
        "embeds": [embed],
        "allowed_mentions": {"parse": []},  # never ping @everyone, @here, roles or users
        "flags": 4096,  # SUPPRESS_NOTIFICATIONS: silent post, no push or desktop alert
    }).encode()
    req = urllib.request.Request(
        webhook, data=body, method="POST",
        headers={"Content-Type": "application/json", "User-Agent": "knightz-devlog-bot"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req) as r:
                print(f"posted {post['slug']} ({r.status})")
                return
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 2:
                time.sleep(float(e.headers.get("Retry-After", "2")))
                continue
            raise


def main():
    webhook = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook:
        sys.exit("DISCORD_WEBHOOK_URL is not set")
    current = load_index()
    force = os.environ.get("FORCE_SLUG", "").strip()
    if force:
        new = [p for p in current if p["slug"] == force]
        if not new:
            sys.exit(f"slug not found: {force}")
    else:
        before = os.environ.get("BEFORE_SHA", "").strip()
        if not before or set(before) == {"0"}:
            print("no previous commit, nothing posted")
            return
        old = {p["slug"] for p in load_index(before)}
        new = [p for p in current if p["slug"] not in old]
    # oldest first so the channel reads in order
    for post in sorted(new, key=lambda p: (p.get("date", ""), p["slug"])):
        send(webhook, post)
        time.sleep(1)
    if not new:
        print("no new posts")


if __name__ == "__main__":
    main()
