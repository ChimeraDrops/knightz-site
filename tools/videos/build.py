"""Build KnightZ video episode pages. Usage: python3 build.py <site_root>"""
import json, sys, html, importlib, os
sys.path.insert(0, os.path.dirname(__file__))
ROOT = sys.argv[1]
SITE = "https://chimeradrops.github.io/knightz-site"
CHANNEL = "https://www.youtube.com/@ksuiegaming9346"

def ts(s):
    m, s = divmod(int(s), 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def esc(s):
    return html.escape(s, quote=True)

NAV = """<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{p}index.html" aria-label="KnightZ home">
      <img src="{p}assets/img/logo.svg" alt="" width="34" height="34">
      <span class="brand-text"><span class="brand-title">KNIGHTZ</span><span class="brand-sub">KSUIE_Gaming</span></span>
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <ul class="nav-links">
      <li><a href="{p}index.html#game">The Game</a></li>
      <li><a href="{p}index.html#world">World</a></li>
      <li><a href="{p}index.html#characters">Characters</a></li>
      <li><a href="{p}index.html#progress">Progress</a></li>
      <li><a href="{p}index.html#gallery">Gallery</a></li>
      <li><a href="{p}devlog.html">Dev Log</a></li>
      <li><a href="{p}videos.html" aria-current="page">Videos</a></li>
      <li><a href="https://discord.gg/72p2FcuExf" target="_blank" rel="noopener">Discord</a></li>
    </ul>
  </div>
</header>"""

FOOT = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{p}index.html"><img src="{p}assets/img/logo.svg" alt="" width="34" height="34"><span class="brand-text"><span class="brand-title">KNIGHTZ</span><span class="brand-sub">The Failing Light</span></span></a>
        <p style="margin-top:16px;max-width:380px">A third-person action adventure in development by KSUIE_Gaming. All content shown is work in progress and subject to change.</p>
      </div>
      <div>
        <h5>Explore</h5>
        <ul><li><a href="{p}index.html#game">The Game</a></li><li><a href="{p}index.html#world">World</a></li><li><a href="{p}index.html#characters">Characters</a></li><li><a href="{p}index.html#progress">Progress</a></li></ul>
      </div>
      <div>
        <h5>Follow</h5>
        <ul><li><a href="{p}index.html#gallery">Gallery</a></li>
      <li><a href="{p}devlog.html">Dev Log</a></li><li><a href="{p}videos.html">Videos</a></li><li><a href="https://www.youtube.com/@ksuiegaming9346" target="_blank" rel="noopener">YouTube</a></li><li><a href="https://discord.gg/72p2FcuExf" target="_blank" rel="noopener">Discord</a></li><li><a href="{p}feed.xml">RSS feed</a></li></ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> KSUIE_Gaming. All rights reserved.</span>
      <span class="rating"><b>M</b> Intended for mature audiences</span>
    </div>
  </div>
</footer>"""

HEADLINKS = """  <link rel="icon" href="{p}assets/img/logo.svg" type="image/svg+xml">
  <link rel="alternate" type="application/rss+xml" title="KnightZ Dev Log" href="{p}feed.xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500;600;700&family=Uncial+Antiqua&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}assets/css/style.css">"""


def jsonld(ep, url):
    parts = []
    ch = ep["chapters"]
    for i, (t, name) in enumerate(ch):
        end = ch[i + 1][0] if i + 1 < len(ch) else ep["seconds"]
        parts.append({"@type": "Clip", "name": name, "startOffset": t, "endOffset": end,
                      "url": f"https://www.youtube.com/watch?v={ep['yt']}&t={t}s"})
    m, s = divmod(ep["seconds"], 60)
    d = {"@context": "https://schema.org", "@graph": [
        {"@type": "VideoObject", "@id": url + "#video", "name": ep["yt_title"],
         "description": ep["ld_desc"], "duration": f"PT{m}M{s}S", "uploadDate": ep["upload"],
         "thumbnailUrl": [ep["thumb_abs"], f"https://i.ytimg.com/vi/{ep['yt']}/hqdefault.jpg"],
         "embedUrl": f"https://www.youtube.com/embed/{ep['yt']}",
         "contentUrl": f"https://www.youtube.com/watch?v={ep['yt']}", "hasPart": parts,
         "author": {"@type": "Organization", "name": "KSUIE Dev Studio", "url": CHANNEL}},
        {"@type": "TechArticle", "headline": f"Episode {ep['n']}: {ep['title']}", "description": ep["meta_desc"],
         "url": url, "image": ep["thumb_abs"], "datePublished": ep["upload"][:10],
         "author": {"@type": "Person", "name": "KSUIE_Gaming"}, "about": ep["tags"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Videos", "item": SITE + "/videos.html"},
            {"@type": "ListItem", "position": 2, "name": f"Episode {ep['n']}", "item": url}]}]}
    return json.dumps(d, indent=2, ensure_ascii=False)


def page(ep, prev_ep, next_ep):
    p = "../"
    url = f"{SITE}/videos/{ep['slug']}.html"
    toc = "\n".join(f'          <li><a href="#{sid}">{esc(lbl)}</a></li>' for sid, lbl in ep["toc"])
    facts = "\n".join(f'          <div class="kv"><span>{esc(k)}</span><b>{esc(v)}</b></div>' for k, v in ep["facts"])
    chaps = "\n".join(f'            <li><button type="button" data-t="{t}"><span class="ts">{ts(t)}</span><span>{esc(n)}</span></button></li>' for t, n in ep["chapters"])
    pills = "".join(f"<span>{esc(x)}</span>" for x in ep["pills"])
    pager = ""
    if prev_ep:
        pager += f'<a class="prev" href="{prev_ep["slug"]}.html"><small>Previous episode</small>Episode {prev_ep["n"]}: {esc(prev_ep["short"])}</a>'
    if next_ep:
        pager += f'<a class="next" href="{next_ep["slug"]}.html"><small>Next episode</small>Episode {next_ep["n"]}: {esc(next_ep["short"])}</a>'
    yt = ep["yt"]
    body = ep["body"].replace("{CHAPTERS}", f'<ol class="chap-list">\n{chaps}\n          </ol>')
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Episode {ep['n']}: {esc(ep['title'])} | KnightZ Videos</title>
  <meta name="description" content="{esc(ep['meta_desc'])}">
  <meta name="theme-color" content="#0e1011">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="video.episode">
  <meta property="og:site_name" content="KnightZ: The Failing Light">
  <meta property="og:title" content="Episode {ep['n']}: {esc(ep['title'])}">
  <meta property="og:description" content="{esc(ep['meta_desc'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{ep['thumb_abs']}">
  <meta property="og:video" content="https://www.youtube.com/embed/{yt}">
  <meta name="twitter:card" content="summary_large_image">
{HEADLINKS.format(p=p)}
  <script type="application/ld+json">
{jsonld(ep, url)}
  </script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

{NAV.format(p=p)}

<main id="main">
  <div class="page-head ep-head">
    <div class="container">
      <div class="crumbs"><a href="{p}videos.html">Videos</a> / Episode {ep['n']}</div>
      <span class="eyebrow">Episode {ep['n']} &middot; AI Game Development</span>
      <h1>{esc(ep['title'])}</h1>
      <p class="muted" style="font-size:14px;margin:-4px 0 14px;font-family:var(--font-ui)">On YouTube: {esc(ep['yt_title'])}</p>
      <p>{esc(ep['lede'])}</p>
      <div class="ep-pills">{pills}</div>
    </div>
  </div>

  <div class="container">
    <div class="ep-player" style="margin-top:36px">
      <div class="yt-frame">
        <iframe id="ep-frame" src="https://www.youtube-nocookie.com/embed/{yt}?rel=0" data-src="https://www.youtube-nocookie.com/embed/{yt}" title="Episode {ep['n']}: {esc(ep['title'])}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
    </div>

    <div class="ep-layout">
      <article class="ep-body">
{body}
        <nav class="ep-pager" aria-label="Episodes">{pager}</nav>
      </article>

      <aside class="ep-aside">
        <div class="side-card toc-card">
          <h4>On this page</h4>
          <ol class="toc">
{toc}
          </ol>
        </div>
        <div class="side-card">
          <h4>Episode facts</h4>
{facts}
        </div>
        <div class="side-card">
          <h4>Watch</h4>
          <a class="btn btn-primary" href="https://www.youtube.com/watch?v={yt}" target="_blank" rel="noopener">Open on YouTube</a>
          <a class="btn btn-ghost" style="margin-top:8px" href="{CHANNEL}?sub_confirmation=1" target="_blank" rel="noopener">Subscribe</a>
        </div>
      </aside>
    </div>
  </div>
</main>

{FOOT.format(p=p)}
<script src="{p}assets/js/main.js"></script>
<script src="{p}assets/js/episode.js"></script>
</body>
</html>
"""


def index_page(eps):
    cards = []
    for ep in reversed(eps):
        cards.append(f"""        <a class="ep-card" href="videos/{ep['slug']}.html" id="episode-{ep['n']}">
          <div class="ep-thumb">
            <img src="{ep['thumb_rel']}" onerror="this.onerror=null;this.src='https://i.ytimg.com/vi/{ep['yt']}/hqdefault.jpg'" alt="Episode {ep['n']} thumbnail: {esc(ep['title'])}" loading="lazy" width="640" height="360">
            <div class="play"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span></div>
            <span class="num">Episode {ep['n']}</span>
            <span class="dur">{ts(ep['seconds'])}</span>
          </div>
          <div class="ep-card-body">
            <h2>{esc(ep['title'])}</h2>
            <p>{esc(ep['card'])}</p>
            <div class="ep-card-meta">{esc(ep['date_h'])} &middot; {len(ep['chapters'])} chapters</div>
            <div class="tags">{''.join(f'<span class="tag">{esc(t)}</span>' for t in ep['tags'][:4])}</div>
            <span class="more">Watch and read the full breakdown &rarr;</span>
          </div>
        </a>""")
    graph = []
    for i, ep in enumerate(reversed(eps)):
        graph.append({"@type": "ListItem", "position": i + 1, "url": f"{SITE}/videos/{ep['slug']}.html",
                      "name": f"Episode {ep['n']}: {ep['title']}"})
    ld = json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "AI Game Development video series",
                     "itemListElement": graph}, indent=2)
    redirect = "{" + ", ".join(f'"#episode-{e["n"]}": "videos/{e["slug"]}.html"' for e in eps) + "}"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Game Development Videos | KnightZ by KSUIE Dev Studio</title>
  <meta name="description" content="Watch the AI Game Development series from KSUIE Dev Studio. Each episode has its own page with the full breakdown: steps, numbers, software, prompts and fixes used to build KnightZ: The Failing Light in Blender and Unreal Engine 5.">
  <meta name="theme-color" content="#0e1011">
  <link rel="canonical" href="{SITE}/videos.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="KnightZ: The Failing Light">
  <meta property="og:title" content="AI Game Development Videos | KSUIE Dev Studio">
  <meta property="og:description" content="Episodes on the AI pipeline and prompting behind KnightZ, each with a full written breakdown.">
  <meta property="og:url" content="{SITE}/videos.html">
  <meta property="og:image" content="{eps[-1]['thumb_abs']}">
  <meta name="twitter:card" content="summary_large_image">
{HEADLINKS.format(p='')}
  <script>(function(){{var m={redirect};if(m[location.hash])location.replace(m[location.hash]);}})();</script>
  <script type="application/ld+json">
{ld}
  </script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

{NAV.format(p='')}

<main id="main">
  <div class="page-head">
    <div class="container">
      <span class="eyebrow">YouTube &middot; KSUIE Dev Studio</span>
      <h1>AI Game Development</h1>
      <p>A video series on the AI pipeline behind KnightZ: The Failing Light. Pick an episode to watch it and read the full breakdown: every step, the numbers, the software, the prompts we typed and the fixes that followed.</p>
      <div class="hero-cta" style="margin-top:26px">
        <a class="btn btn-primary" href="{CHANNEL}?sub_confirmation=1" target="_blank" rel="noopener">Subscribe on YouTube</a>
        <a class="btn btn-ghost" href="https://www.youtube.com/playlist?list=PLaMPwZNwIm7g" target="_blank" rel="noopener">Open the Playlist</a>
      </div>
    </div>
  </div>

  <section style="border-bottom:none;padding-top:56px">
    <div class="container">
      <div class="ep-grid">
{chr(10).join(cards)}
      </div>

      <div class="card" style="margin-top:56px">
        <h3>More on the build</h3>
        <p>The <a href="devlog.html">Dev Log</a> covers daily progress on characters, weapons, terrain and tools. The <a href="index.html#gallery">Gallery</a> shows the latest work in progress.</p>
      </div>
    </div>
  </section>
</main>

{FOOT.format(p='')}
<script src="assets/js/main.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    eps = [importlib.import_module(f"ep{i}").EP for i in (1, 2, 3)]  # add new episode numbers here
    os.makedirs(os.path.join(ROOT, "videos"), exist_ok=True)
    for i, ep in enumerate(eps):
        prev_ep = eps[i - 1] if i > 0 else None
        next_ep = eps[i + 1] if i + 1 < len(eps) else None
        out = page(ep, prev_ep, next_ep)
        open(os.path.join(ROOT, "videos", ep["slug"] + ".html"), "w").write(out)
        print("wrote", ep["slug"], len(out))
    open(os.path.join(ROOT, "videos.html"), "w").write(index_page(eps))
    print("wrote videos.html")
