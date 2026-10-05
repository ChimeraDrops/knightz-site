/* KnightZ dev log: manifest loader, list page, post page */
(function () {
  "use strict";
  var MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  var cache = null;

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function parts(iso) { var p = iso.split("-"); return { y: +p[0], m: +p[1], d: +p[2] }; }
  function fmtDate(iso) { var p = parts(iso); return MONTHS[p.m - 1] + " " + p.d + ", " + p.y; }

  function loadPosts() {
    if (cache) return Promise.resolve(cache);
    return fetch("posts/index.json", { cache: "no-cache" })
      .then(function (r) { if (!r.ok) throw new Error("manifest"); return r.json(); })
      .then(function (list) {
        cache = list.slice().sort(function (a, b) {
          return a.date < b.date ? 1 : a.date > b.date ? -1 : (b.order || 0) - (a.order || 0);
        });
        return cache;
      });
  }

  function postCard(p) {
    var d = parts(p.date);
    return '<a class="post-card" href="post.html?p=' + encodeURIComponent(p.slug) + '">' +
      '<div class="post-date"><span class="d">' + d.d + '</span><span class="m">' + MONTHS[d.m - 1] + " " + d.y + "</span></div>" +
      "<div><h3>" + esc(p.title) + "</h3><p>" + esc(p.summary) + '</p><div class="tags">' +
      (p.tags || []).map(function (t) { return '<span class="tag">' + esc(t) + "</span>"; }).join("") +
      "</div></div></a>";
  }

  window.KZ = { loadPosts: loadPosts, postCard: postCard, fmtDate: fmtDate, esc: esc };

  /* ---------- List page ---------- */
  var listEl = document.getElementById("devlog-list");
  if (listEl) {
    var filtersEl = document.getElementById("devlog-filters");
    loadPosts().then(function (posts) {
      var tags = {};
      posts.forEach(function (p) { (p.tags || []).forEach(function (t) { tags[t] = (tags[t] || 0) + 1; }); });
      var names = Object.keys(tags).sort();
      var params = new URLSearchParams(location.search);
      var current = params.get("tag") || "all";
      function render() {
        filtersEl.innerHTML = ['<button class="filter' + (current === "all" ? " active" : "") + '" data-tag="all">All (' + posts.length + ")</button>"]
          .concat(names.map(function (t) {
            return '<button class="filter' + (current === t ? " active" : "") + '" data-tag="' + esc(t) + '">' + esc(t) + " (" + tags[t] + ")</button>";
          })).join("");
        var shown = current === "all" ? posts : posts.filter(function (p) { return (p.tags || []).indexOf(current) > -1; });
        listEl.innerHTML = shown.length ? shown.map(postCard).join("") : '<p class="muted">No entries with this tag yet.</p>';
        var count = document.getElementById("devlog-count");
        if (count) count.textContent = posts.length + " entries. Newest first.";
      }
      filtersEl.addEventListener("click", function (e) {
        var b = e.target.closest("button[data-tag]");
        if (!b) return;
        current = b.getAttribute("data-tag");
        var u = new URL(location.href);
        if (current === "all") u.searchParams.delete("tag"); else u.searchParams.set("tag", current);
        history.replaceState(null, "", u);
        render();
      });
      render();
    }).catch(function () {
      listEl.innerHTML = '<p class="muted">Could not load the dev log. Serve the site over HTTP (GitHub Pages, or run <code>python -m http.server</code> in the site folder).</p>';
    });
  }

  /* ---------- Post page ---------- */
  var postEl = document.getElementById("post");
  if (postEl) {
    var slug = new URLSearchParams(location.search).get("p");
    loadPosts().then(function (posts) {
      var i = -1;
      posts.forEach(function (p, k) { if (p.slug === slug) i = k; });
      if (i < 0) throw new Error("missing");
      var p = posts[i];
      return fetch("posts/" + encodeURIComponent(p.slug) + ".md", { cache: "no-cache" })
        .then(function (r) { if (!r.ok) throw new Error("md"); return r.text(); })
        .then(function (md) {
          md = md.replace(/^---[\s\S]*?\n---\s*\n/, "");
          var html = window.marked ? window.marked.parse(md) : "<pre>" + esc(md) + "</pre>";
          document.title = p.title + " | KnightZ Dev Log";
          var desc = document.querySelector('meta[name="description"]');
          if (desc) desc.setAttribute("content", p.summary);
          var newer = posts[i - 1], older = posts[i + 1];
          postEl.innerHTML =
            '<div class="article-meta"><a href="devlog.html">Dev Log</a><span>/</span><time datetime="' + p.date + '">' + fmtDate(p.date) + "</time>" +
            (p.author ? "<span>/</span><span>" + esc(p.author) + "</span>" : "") + "</div>" +
            '<h1 class="title">' + esc(p.title) + "</h1>" +
            '<div class="tags" style="margin-bottom:34px">' + (p.tags || []).map(function (t) {
              return '<a class="tag" href="devlog.html?tag=' + encodeURIComponent(t) + '">' + esc(t) + "</a>";
            }).join("") + "</div>" +
            '<div class="prose">' + html + "</div>" +
            '<nav class="post-nav" aria-label="More entries">' +
            (older ? '<a href="post.html?p=' + encodeURIComponent(older.slug) + '"><small>Previous entry</small>' + esc(older.title) + "</a>" : "<span></span>") +
            (newer ? '<a class="next" href="post.html?p=' + encodeURIComponent(newer.slug) + '"><small>Next entry</small>' + esc(newer.title) + "</a>" : "<span></span>") +
            "</nav>";
          window.scrollTo(0, 0);
        });
    }).catch(function () {
      postEl.innerHTML = '<h1 class="title">Entry not found</h1><p class="muted">This dev log entry does not exist or could not be loaded. <a href="devlog.html">Back to the dev log</a>.</p>';
    });
  }
})();
