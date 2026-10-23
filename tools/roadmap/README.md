# RoadMap generator

`python3 tools/roadmap/build.py .` writes `roadmap.html` and one page per checklist in `roadmap/`.

- Data: `tools/roadmap/roadmap.json` (checklists, groups, items, step states `done` / `wip` / `todo` / `na`, image paths).
- Images: `assets/img/roadmap/<checklist>/<name>.jpg` with `<name>_t.jpg` thumbnails. Thumbnails open the full image in a lightbox (`assets/js/roadmap.js`).
- Shared header and footer: `tools/site_common.py` (also used by `tools/videos/build.py`).
- To update progress: edit the step states in `roadmap.json`, add images, rebuild, commit.
