"""Build the RoadMap: roadmap.html (index) and roadmap/<slug>.html (one page per checklist).

Usage: python3 tools/roadmap/build.py <site_root>
Data: tools/roadmap/roadmap.json. Step states: done, wip, todo, na.
"""
import html, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from site_common import HEADLINKS, SITE, nav, foot

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
DATA = json.load(open(os.path.join(os.path.dirname(__file__), "roadmap.json")))
VAL = {"done": 1.0, "wip": 0.5, "todo": 0.0}
LABEL = {"done": "Done", "wip": "In progress", "todo": "To do", "na": "Not needed"}


def esc(s):
    return html.escape(str(s), quote=True)


def item_state(it):
    st = [s for s in it["steps"] if s != "na"]
    if st and all(s == "done" for s in st):
        return "done"
    if any(s in ("done", "wip") for s in st):
        return "wip"
    return "todo"


def score(items):
    n = sum(1 for it in items for s in it["steps"] if s != "na")
    v = sum(VAL[s] for it in items for s in it["steps"] if s != "na")
    return (v / n if n else 0.0), n


def stats(items):
    pct, _ = score(items)
    done = sum(1 for it in items if item_state(it) == "done")
    wip = sum(1 for it in items if item_state(it) == "wip")
    return {"pct": round(pct * 100), "done": done, "wip": wip, "todo": len(items) - done - wip, "total": len(items)}


def all_items(cl):
    return [it for g in cl["groups"] for it in g["items"]]


def bar(pct, cls=""):
    return f'<div class="rm-bar {cls}" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="{pct}"><span style="width:{pct}%"></span></div>'


CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 16.2 5.3 12l-1.4 1.4 5.6 5.6 11-11-1.4-1.4z"/></svg>'
HALF = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="5"/></svg>'


def step_chips(cl, it):
    out = []
    for lab, s in zip(cl["steps"], it["steps"]):
        icon = CHECK if s == "done" else HALF if s == "wip" else ""
        out.append(f'<li class="s-{s}" title="{esc(lab)}: {LABEL[s]}"><i>{icon}</i>{esc(lab)}</li>')
    return '<ul class="rm-steps">' + "".join(out) + "</ul>"


def thumbs(it, p, cols=False):
    if not it["imgs"]:
        return f'<div class="rm-ph"><span>{esc(it.get("code") or "Not built yet")}</span></div>'
    out = []
    for i, im in enumerate(it["imgs"]):
        out.append(f'<a class="rm-shot" href="{p}{im["src"]}" data-lb="{esc(im["alt"])}"><img src="{p}{im["thumb"]}" alt="{esc(im["alt"])}" loading="lazy"></a>')
    return f'<div class="rm-thumbs n{min(len(it["imgs"]), 3)}{" cols" if cols else ""}">' + "".join(out) + "</div>"


def row(cl, it, p):
    stt = item_state(it)
    pct, _ = score([it])
    code = f'<span class="rm-code">{esc(it["code"])}</span>' if it.get("code") else ""
    sub = f'<p>{esc(it["sub"])}</p>' if it.get("sub") else ""
    return f"""        <article class="rm-item" data-state="{stt}" data-name="{esc(it['name'].lower())}">
          {thumbs(it, p, cl.get('thumbs') == 'cols')}
          <div class="rm-main">
            <h3><span class="rm-dot {stt}">{CHECK if stt == 'done' else ''}</span>{esc(it['name'])}{code}</h3>
            {sub}
            {step_chips(cl, it)}
          </div>
          <div class="rm-pct"><b>{round(pct * 100)}%</b><span>{LABEL[stt]}</span></div>
        </article>"""


def tile(cl, it, p):
    stt = item_state(it)
    code = f'<span class="rm-code">{esc(it["code"])}</span>' if it.get("code") else ""
    sub = f'<p>{esc(it["sub"])}</p>' if it.get("sub") else ""
    return f"""        <article class="rm-tile" data-state="{stt}" data-name="{esc(it['name'].lower())}">
          {thumbs(it, p)}
          <div class="rm-tile-body">
            <h3><span class="rm-dot {stt}">{CHECK if stt == 'done' else ''}</span>{esc(it['name'])}</h3>
            <div class="rm-meta">{code}{sub}</div>
            {step_chips(cl, it)}
          </div>
        </article>"""


def head(title, desc, url, image, p):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="theme-color" content="#0e1011">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="KnightZ: The Failing Light">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/{image}">
  <meta name="twitter:card" content="summary_large_image">
{HEADLINKS.format(p=p)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

{nav(p, 'roadmap')}
"""


def tail(p):
    return f"""
{foot(p)}
<script src="{p}assets/js/main.js"></script>
<script src="{p}assets/js/roadmap.js"></script>
</body>
</html>
"""


def checklist_page(cl, prev_cl, next_cl):
    p = "../"
    items = all_items(cl)
    s = stats(items)
    use_tiles = len(cl["steps"]) <= 3
    url = f"{SITE}/roadmap/{cl['slug']}.html"
    desc = f"KnightZ RoadMap checklist: {cl['title']}. {s['done']} of {s['total']} complete. " + cl["intro"][:150]
    groups_html = []
    toc = []
    for gi, g in enumerate(cl["groups"]):
        gid = g.get("id") or f"g{gi + 1}"
        gs = stats(g["items"])
        body = "\n".join((tile if use_tiles else row)(cl, it, p) for it in g["items"])
        intro = f'<p class="rm-gintro">{esc(g["intro"])}</p>' if g.get("intro") else ""
        groups_html.append(f"""      <section class="rm-group" id="{gid}">
        <div class="rm-ghead">
          <h2>{esc(g['title'])}</h2>
          <div class="rm-gstat"><span>{gs['done']} of {gs['total']} complete</span>{bar(gs['pct'], 'sm')}<b>{gs['pct']}%</b></div>
        </div>
        {intro}
        <div class="{'rm-tiles' if use_tiles else 'rm-list'}">
{body}
        </div>
      </section>""")
        toc.append(f'<a href="#{gid}">{esc(g["title"])} <span>{gs["done"]}/{gs["total"]}</span></a>')
    legend = ""
    if cl.get("legend"):
        legend = '<dl class="rm-legend">' + "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in cl["legend"].items()) + "</dl>"
    links = ""
    if cl.get("links"):
        links = '<div class="rm-links"><h4>Read more</h4><ul>' + "".join(f'<li><a href="{p}{esc(u)}">{esc(t)}</a></li>' for t, u in cl["links"]) + "</ul></div>"
    pager = ""
    if prev_cl:
        pager += f'<a class="prev" href="{prev_cl["slug"]}.html"><small>Previous checklist</small>{esc(prev_cl["title"])}</a>'
    if next_cl:
        pager += f'<a class="next" href="{next_cl["slug"]}.html"><small>Next checklist</small>{esc(next_cl["title"])}</a>'
    steps_list = "".join(f"<li>{esc(x)}</li>" for x in cl["steps"])
    return head(f"{cl['title']} | KnightZ RoadMap", desc, url, cl["cover"], p) + f"""
<main id="main">
  <div class="page-head rm-head">
    <div class="container">
      <div class="crumbs"><a href="{p}roadmap.html">RoadMap</a> / {esc(cl['title'])}</div>
      <span class="eyebrow">{esc(cl['eyebrow'])} &middot; Checklist</span>
      <h1>{esc(cl['title'])}</h1>
      <p>{esc(cl['intro'])}</p>
      <div class="rm-summary">
        <div class="rm-big"><b>{s['pct']}%</b><span>of all steps</span></div>
        <div class="rm-sumbar">{bar(s['pct'])}
          <div class="rm-counts"><span class="c-done">{s['done']} complete</span><span class="c-wip">{s['wip']} in progress</span><span class="c-todo">{s['todo']} not started</span><span>{s['total']} items</span></div>
        </div>
      </div>
    </div>
  </div>

  <div class="container rm-wrap">
    <div class="rm-toolbar" role="toolbar" aria-label="Filter items">
      <div class="rm-filters">
        <button type="button" class="on" data-f="all">All <span>{s['total']}</span></button>
        <button type="button" data-f="done">Complete <span>{s['done']}</span></button>
        <button type="button" data-f="wip">In progress <span>{s['wip']}</span></button>
        <button type="button" data-f="todo">Not started <span>{s['todo']}</span></button>
      </div>
      <input type="search" class="rm-search" placeholder="Search this checklist" aria-label="Search this checklist">
    </div>
    <div class="rm-layout">
      <div class="rm-content">
{chr(10).join(groups_html)}
        <p class="rm-empty" hidden>No items match.</p>
        <nav class="ep-pager" aria-label="Checklists">{pager}</nav>
      </div>
      <aside class="rm-aside">
        <div class="side-card">
          <h4>Sections</h4>
          <div class="rm-toc">{''.join(toc)}</div>
        </div>
        <div class="side-card">
          <h4>Steps per item</h4>
          <ol class="rm-steplist">{steps_list}</ol>
          {legend}
        </div>
        <div class="side-card rm-key">
          <h4>Key</h4>
          <ul class="rm-steps"><li class="s-done"><i>{CHECK}</i>Done</li><li class="s-wip"><i>{HALF}</i>In progress</li><li class="s-todo"><i></i>To do</li><li class="s-na"><i></i>Not needed</li></ul>
          <p>Updated {esc(DATA['updated'])}. Click any image to see it full size.</p>
        </div>
        {('<div class="side-card">' + links + '</div>') if links else ''}
      </aside>
    </div>
  </div>
</main>
""" + tail(p)


def index_page(cls):
    p = ""
    every = [it for cl in cls for it in all_items(cl)]
    tot = stats(every)
    cards = []
    sections = {}
    for cl in cls:
        s = stats(all_items(cl))
        sections.setdefault(cl["eyebrow"], []).append(f"""        <a class="rm-card" href="roadmap/{cl['slug']}.html">
          <div class="rm-card-img"><img src="{cl['cover'].replace('.jpg', '_t.jpg') if os.path.exists(os.path.join(ROOT, cl['cover'].replace('.jpg', '_t.jpg'))) else cl['cover']}" alt="" loading="lazy"><span class="rm-card-pct">{s['pct']}%</span></div>
          <div class="rm-card-body">
            <span class="rm-card-eyebrow">{esc(cl['eyebrow'])}</span>
            <h2>{esc(cl['title'])}</h2>
            {bar(s['pct'])}
            <div class="rm-card-meta"><span>{s['done']} of {s['total']} complete</span><span>{len(cl['steps'])} steps each</span></div>
            <p>{esc(cl['intro'].split('. ')[0].rstrip('.'))}.</p>
            <span class="more">Open checklist &rarr;</span>
          </div>
        </a>""")
    for k, v in sections.items():
        cards.append(f'      <h2 class="rm-sec">{esc(k)}</h2>\n      <div class="rm-cards">\n' + "\n".join(v) + "\n      </div>")
    rows = "".join(f'<tr><td><a href="roadmap/{cl["slug"]}.html">{esc(cl["title"])}</a></td><td class="num">{stats(all_items(cl))["done"]}</td><td class="num">{stats(all_items(cl))["total"]}</td><td>{bar(stats(all_items(cl))["pct"], "sm")}</td><td class="num">{stats(all_items(cl))["pct"]}%</td></tr>' for cl in cls)
    ld = json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "KnightZ RoadMap checklists",
                     "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/roadmap/{c['slug']}.html", "name": c["title"]} for i, c in enumerate(cls)]}, indent=2)
    return head("RoadMap | KnightZ: The Failing Light", "Every development checklist for KnightZ in one place: heroes, animations, region maps, trees, plants, sky and seasons, buildings and props, with images of finished work and progress on each step.", f"{SITE}/roadmap.html", cls[0]["cover"], p).replace("</head>", f'  <script type="application/ld+json">\n{ld}\n  </script>\n</head>') + f"""
<main id="main">
  <div class="page-head rm-head">
    <div class="container">
      <span class="eyebrow">Development &middot; RoadMap</span>
      <h1>RoadMap</h1>
      <p>The checklists we build KnightZ by, published as we work. Each one has its own page with every item, every step and a picture of the finished piece. Click a checklist to open it.</p>
      <div class="rm-summary">
        <div class="rm-big"><b>{tot['pct']}%</b><span>of all tracked steps</span></div>
        <div class="rm-sumbar">{bar(tot['pct'])}
          <div class="rm-counts"><span class="c-done">{tot['done']} items complete</span><span class="c-wip">{tot['wip']} in progress</span><span class="c-todo">{tot['todo']} not started</span><span>{len(cls)} checklists</span></div>
        </div>
      </div>
    </div>
  </div>

  <section style="border-bottom:none;padding-top:48px">
    <div class="container">
{chr(10).join(cards)}

      <h2 class="rm-sec">All checklists at a glance</h2>
      <div class="tbl rm-table"><table><thead><tr><th>Checklist</th><th class="num">Complete</th><th class="num">Items</th><th>Progress</th><th class="num">Steps</th></tr></thead><tbody>{rows}</tbody></table></div>

      <div class="card" style="margin-top:48px">
        <h3>How the checklists work</h3>
        <p>Every item moves through the same steps as the rest of its checklist. A filled check means the step is done, a dot means it is in progress, and an empty box means it has not started. Items that do not need a step (a hero with no beard, for example) show it greyed out. Pages are regenerated from the project records with each update; the <a href="devlog.html">Dev Log</a> covers the day-to-day work behind them.</p>
      </div>
    </div>
  </section>
</main>
""" + tail(p)


if __name__ == "__main__":
    cls = DATA["checklists"]
    os.makedirs(os.path.join(ROOT, "roadmap"), exist_ok=True)
    for i, cl in enumerate(cls):
        out = checklist_page(cl, cls[i - 1] if i > 0 else None, cls[i + 1] if i + 1 < len(cls) else None)
        open(os.path.join(ROOT, "roadmap", cl["slug"] + ".html"), "w").write(out)
        print("wrote roadmap/" + cl["slug"] + ".html", len(out))
    open(os.path.join(ROOT, "roadmap.html"), "w").write(index_page(cls))
    print("wrote roadmap.html")
