"""Shared header, footer and head links for generated pages (videos, roadmap).

nav(p, current): p is the path prefix to the site root ('' or '../'); current is 'videos', 'roadmap' or ''.
"""

SITE = "https://chimeradrops.github.io/knightz-site"
CHANNEL = "https://www.youtube.com/@ksuiegaming9346"

HEADLINKS = """  <link rel="icon" href="{p}assets/img/logo.svg" type="image/svg+xml">
  <link rel="alternate" type="application/rss+xml" title="KnightZ Dev Log" href="{p}feed.xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500;600;700&family=Uncial+Antiqua&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}assets/css/style.css">"""


def nav(p, current=""):
    def cur(k):
        return ' aria-current="page"' if k == current else ""
    return f"""<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{p}index.html" aria-label="KnightZ home">
      <img src="{p}assets/img/logo.svg" alt="" width="34" height="34">
      <span class="brand-text"><span class="brand-title">KNIGHTZ</span><span class="brand-sub">KSUIE_Gaming</span></span>
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <ul class="nav-links">
      <li><a href="{p}index.html#game">The Game</a></li>
      <li><a href="{p}lore.html"{cur('lore')}>Lore</a></li>
      <li><a href="{p}index.html#world">World</a></li>
      <li><a href="{p}index.html#characters">Characters</a></li>
      <li><a href="{p}index.html#progress">Progress</a></li>
      <li><a href="{p}index.html#gallery">Gallery</a></li>
      <li><a href="{p}devlog.html">Dev Log</a></li>
      <li><a href="{p}videos.html"{cur('videos')}>Videos</a></li>
      <li><a href="{p}roadmap.html"{cur('roadmap')}>RoadMap</a></li>
      <li><a href="https://discord.gg/72p2FcuExf" target="_blank" rel="noopener">Discord</a></li>
    </ul>
  </div>
</header>"""


def foot(p):
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{p}index.html"><img src="{p}assets/img/logo.svg" alt="" width="34" height="34"><span class="brand-text"><span class="brand-title">KNIGHTZ</span><span class="brand-sub">The Failing Light</span></span></a>
        <p style="margin-top:16px;max-width:380px">A third-person action adventure in development by KSUIE_Gaming. All content shown is work in progress and subject to change.</p>
      </div>
      <div>
        <h5>Explore</h5>
        <ul><li><a href="{p}index.html#game">The Game</a></li><li><a href="{p}lore.html">Lore</a></li><li><a href="{p}index.html#world">World</a></li><li><a href="{p}index.html#characters">Characters</a></li><li><a href="{p}index.html#progress">Progress</a></li><li><a href="{p}roadmap.html">RoadMap</a></li></ul>
      </div>
      <div>
        <h5>Follow</h5>
        <ul><li><a href="{p}index.html#gallery">Gallery</a></li><li><a href="{p}devlog.html">Dev Log</a></li><li><a href="{p}videos.html">Videos</a></li><li><a href="{CHANNEL}" target="_blank" rel="noopener">YouTube</a></li><li><a href="https://discord.gg/72p2FcuExf" target="_blank" rel="noopener">Discord</a></li><li><a href="{p}feed.xml">RSS feed</a></li></ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> KSUIE_Gaming. All rights reserved.</span>
      <span class="rating"><b>M</b> Intended for mature audiences</span>
    </div>
  </div>
</footer>"""
