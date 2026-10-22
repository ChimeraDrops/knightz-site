/* KnightZ episode pages: chapter seek, copy buttons, section highlight */
(function () {
  "use strict";
  var frame = document.getElementById("ep-frame");
  function seek(t) {
    if (!frame) return;
    var base = frame.getAttribute("data-src");
    frame.src = base + "?start=" + t + "&autoplay=1&rel=0";
    frame.scrollIntoView({ behavior: "smooth", block: "center" });
  }
  document.querySelectorAll("[data-t]").forEach(function (b) {
    b.addEventListener("click", function () { seek(parseInt(b.getAttribute("data-t"), 10) || 0); });
  });
  document.querySelectorAll(".prompt").forEach(function (box) {
    var btn = box.querySelector("button.copy");
    var pre = box.querySelector("pre");
    if (!btn || !pre) return;
    btn.addEventListener("click", function () {
      var txt = pre.innerText;
      var done = function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Copy"; }, 1600); };
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(txt).then(done, function () {}); return; }
      } catch (e) {}
      var ta = document.createElement("textarea"); ta.value = txt; document.body.appendChild(ta); ta.select();
      try { document.execCommand("copy"); done(); } catch (e) {}
      document.body.removeChild(ta);
    });
  });
  var links = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
  if ("IntersectionObserver" in window && links.length) {
    var map = {};
    links.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && map[en.target.id]) {
          links.forEach(function (a) { a.classList.remove("active"); });
          map[en.target.id].classList.add("active");
        }
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    document.querySelectorAll(".ep-body section[id]").forEach(function (s) { io.observe(s); });
  }
})();
