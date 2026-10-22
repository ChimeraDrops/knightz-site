# Episode page generator

`python3 tools/videos/build.py .` (run from the repo root) rebuilds `videos.html` and `videos/<slug>.html`.

- `ep<N>.py`: one module per episode (title, YouTube id, chapters, facts, page body).
- `h.py`: helpers for figures, prompt blocks with copy buttons, tables, stat rows.
- To add an episode: copy `ep3.py` to `ep4.py`, edit, then add 4 to the tuple in `build.py`.
- Images: `assets/img/videos/ep<N>/`. Styles: "Episode page" block in `assets/css/style.css`. Script: `assets/js/episode.js`.
- Update `sitemap.xml` with the new page.
