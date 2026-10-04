# KnightZ: The Failing Light | Dev Site

Promotional and dev log website for KnightZ (KSUIE_Gaming). Static HTML, CSS and JavaScript. No build step. Runs on GitHub Pages.

## Publish on GitHub Pages

1. Create a repository (for example `knightz`) and upload every file in this folder, including `.nojekyll`.
2. Repository **Settings > Pages > Build and deployment**: Source = *Deploy from a branch*, Branch = `main`, folder `/ (root)`. Save.
3. The site goes live at `https://<username>.github.io/<repo>/` within a minute or two.
4. Open `tools/new_post.py` and set `SITE_URL` to that address, then run `python tools/new_post.py --feed` once so the RSS links are correct.
5. Optional: for link previews on social media, add `assets/img/og-card.png` (1200 x 630). One is included.

## Daily dev log entry

```
python tools/new_post.py "Dev Log #10: The yew bow" --tags weapons,props --summary "One sentence shown on the card."
```

This creates `posts/<date>-<slug>.md`, adds it to `posts/index.json` and rebuilds `feed.xml`. Write the entry in Markdown in the new file, then commit and push:

```
git add -A
git commit -m "Dev log: The yew bow"
git push
```

Without Python: copy any file in `posts/`, rename it, and add a matching entry at the top of `posts/index.json` (slug = file name without `.md`).

### Images in posts

Put images in `assets/img/devlog/` and reference them in Markdown:

```
![Yew bow, front and side](assets/img/devlog/bow_front.jpg)
```

Use JPG or WebP around 1600 px wide to keep pages fast.

## Media gallery

The home page gallery stays hidden until images are listed. Add files to `assets/img/gallery/` and list them in `assets/data/gallery.json`:

```json
[
  { "src": "assets/img/gallery/bedwyr_head.jpg", "caption": "Sir Bedwyr, head and hair" },
  { "src": "assets/img/gallery/weapons_lineup.jpg", "caption": "The weapon set" }
]
```

## Character portraits

Each character card in `index.html` has `data-img=""`. Put a render path there (for example `data-img="assets/img/gallery/bedwyr_head.jpg"`) to replace the placeholder crest.

## Updating progress

The stats, progress rows and roadmap are plain HTML in `index.html` under the `PROGRESS` and `ROADMAP` comments. Change the badge class to move an item: `done`, `wip` or `plan`.

## Preview locally

The dev log loads Markdown with `fetch`, which browsers block on `file://`. Run a local server in this folder:

```
python -m http.server 8000
```

Then open http://localhost:8000.

## Structure

```
index.html        Home: hero, game, pillars, seasons, world map, characters, progress, dev log, roadmap
devlog.html       All entries with tag filters
post.html         Single entry (post.html?p=<slug>)
404.html          Not found page
feed.xml          RSS (built by tools/new_post.py)
posts/            Markdown entries + index.json manifest
assets/css/       style.css
assets/js/        main.js (site), devlog.js (dev log)
assets/img/       logo, hero art, devlog/, gallery/
assets/data/      gallery.json
tools/            new_post.py
```
