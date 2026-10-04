#!/usr/bin/env python3
"""KnightZ dev log helper.

Create today's entry:
    python tools/new_post.py "Dev Log #10: The yew bow" --tags weapons,props --summary "One line for the card."

This writes posts/<date>-<slug>.md (open it and write the entry in Markdown),
adds the entry to posts/index.json and rebuilds feed.xml.

After editing an existing post's title/summary/tags in posts/index.json, rebuild the feed only:
    python tools/new_post.py --feed

Options:
    --date YYYY-MM-DD   default: today
    --slug my-slug      default: built from the title
    --author NAME       default: KSUIE_Gaming
No third-party packages needed (Python 3.8+).
"""
import argparse, datetime, json, os, re, sys
from email.utils import format_datetime
from xml.sax.saxutils import escape

# Set this to your GitHub Pages address (used for RSS links).
SITE_URL = "https://YOUR-USERNAME.github.io/knightz"
SITE_TITLE = "KnightZ: The Failing Light | Dev Log"
SITE_DESC = "Daily development updates on KnightZ: The Failing Light by KSUIE_Gaming."

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "posts")
INDEX = os.path.join(POSTS, "index.json")
FEED = os.path.join(ROOT, "feed.xml")


def slugify(s):
    s = re.sub(r"^dev log #\d+:\s*", "", s.strip(), flags=re.I)
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60] or "entry"


def load():
    with open(INDEX, encoding="utf-8") as f:
        return json.load(f)


def save(items):
    items.sort(key=lambda p: p["date"], reverse=True)
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
        f.write("\n")


def build_feed(items):
    base = SITE_URL.rstrip("/")
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<rss version="2.0"><channel>',
           "<title>%s</title>" % escape(SITE_TITLE),
           "<link>%s/devlog.html</link>" % base,
           "<description>%s</description>" % escape(SITE_DESC),
           "<language>en</language>"]
    for p in sorted(items, key=lambda p: p["date"], reverse=True)[:30]:
        d = datetime.datetime.strptime(p["date"], "%Y-%m-%d").replace(hour=12, tzinfo=datetime.timezone.utc)
        url = "%s/post.html?p=%s" % (base, p["slug"])
        out += ["<item>",
                "<title>%s</title>" % escape(p["title"]),
                "<link>%s</link>" % escape(url),
                '<guid isPermaLink="false">%s</guid>' % escape(p["slug"]),
                "<pubDate>%s</pubDate>" % format_datetime(d),
                "<description>%s</description>" % escape(p.get("summary", "")),
                "</item>"]
    out.append("</channel></rss>")
    with open(FEED, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")


def main():
    ap = argparse.ArgumentParser(description="Create a KnightZ dev log entry.")
    ap.add_argument("title", nargs="?")
    ap.add_argument("--summary", default="")
    ap.add_argument("--tags", default="")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--slug")
    ap.add_argument("--author", default="KSUIE_Gaming")
    ap.add_argument("--feed", action="store_true", help="only rebuild feed.xml")
    a = ap.parse_args()

    items = load()
    if a.feed:
        build_feed(items)
        print("feed.xml rebuilt (%d entries)" % len(items))
        return
    if not a.title:
        ap.error("title is required")

    slug = a.slug or "%s-%s" % (a.date, slugify(a.title))
    if any(p["slug"] == slug for p in items):
        sys.exit("A post with slug '%s' already exists." % slug)
    path = os.path.join(POSTS, slug + ".md")
    tags = [t.strip() for t in a.tags.split(",") if t.strip()]
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\ntitle: %s\ndate: %s\n---\n\n" % (a.title, a.date))
        f.write("Opening paragraph: what was worked on today.\n\n## What was built\n\n- \n\n## Next\n\n")
    items.append({"slug": slug, "title": a.title, "date": a.date,
                  "summary": a.summary or "Summary for the card.", "tags": tags, "author": a.author})
    save(items)
    build_feed(items)
    print("Created posts/%s.md" % slug)
    print("Updated posts/index.json and feed.xml")
    print("Images: put them in assets/img/devlog/ and use ![Caption](assets/img/devlog/file.jpg)")


if __name__ == "__main__":
    main()
