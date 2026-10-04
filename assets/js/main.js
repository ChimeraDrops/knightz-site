/* KnightZ dev site: shared behaviour */
(function () {
  "use strict";

  /* ---------- Nav toggle ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") links.classList.remove("open");
    });
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Character portraits ---------- */
  document.querySelectorAll(".char-portrait[data-initial]").forEach(function (box) {
    var img = box.getAttribute("data-img");
    if (img) {
      var i = document.createElement("img");
      i.src = img; i.alt = box.getAttribute("data-alt") || ""; i.loading = "lazy";
      box.insertBefore(i, box.firstChild);
      return;
    }
    var ch = box.getAttribute("data-initial");
    var hue = box.getAttribute("data-tone") || "#b4432e";
    var svg =
      '<svg viewBox="0 0 400 300" role="img" aria-label="Portrait placeholder" xmlns="http://www.w3.org/2000/svg">' +
      '<defs><radialGradient id="g' + ch + '" cx="50%" cy="40%" r="70%"><stop offset="0" stop-color="#2a2f33"/><stop offset="1" stop-color="#121516"/></radialGradient></defs>' +
      '<rect width="400" height="300" fill="url(#g' + ch + ')"/>' +
      '<g fill="none" stroke="#3a4146" stroke-width="1">' +
      '<circle cx="200" cy="150" r="104"/><circle cx="200" cy="150" r="94" stroke-dasharray="2 6"/></g>' +
      '<path d="M200 70 L262 92 L262 158 Q262 214 200 238 Q138 214 138 158 L138 92 Z" fill="#191d1f" stroke="' + hue + '" stroke-width="2"/>' +
      '<text x="200" y="182" text-anchor="middle" font-family="Uncial Antiqua, Georgia, serif" font-size="88" fill="#e6dcc5">' + ch + "</text>" +
      "</svg>";
    box.insertAdjacentHTML("afterbegin", svg);
  });

  /* ---------- Latest dev log posts on the home page ---------- */
  var latest = document.getElementById("latest-posts");
  if (latest && window.KZ && KZ.loadPosts) {
    KZ.loadPosts().then(function (posts) {
      latest.innerHTML = posts.slice(0, 3).map(KZ.postCard).join("");
    }).catch(function () {
      latest.innerHTML = '<p class="muted">Dev log entries load when the site is served over HTTP (GitHub Pages or a local server).</p>';
    });
  }

  /* ---------- Gallery (hidden until images are listed) ---------- */
  var gal = document.getElementById("gallery");
  if (gal) {
    fetch("assets/data/gallery.json", { cache: "no-cache" })
      .then(function (r) { return r.json(); })
      .then(function (items) {
        if (!items || !items.length) return;
        gal.querySelector(".gallery").innerHTML = items.map(function (it) {
          return '<figure><a href="' + it.src + '" target="_blank" rel="noopener"><img src="' + it.src +
            '" alt="' + (it.caption || "") + '" loading="lazy"></a><figcaption>' + (it.caption || "") + "</figcaption></figure>";
        }).join("");
        gal.hidden = false;
      }).catch(function () {});
  }

  /* ---------- Region map ---------- */
  var mapEl = document.getElementById("region-map");
  if (mapEl) drawMap(mapEl);

  function drawMap(el) {
    var R = [
      { c: "M01", d: "r", n: "Severn Vale", r: "The manor. Hub of the game.", lat: 52.633, lon: -2.600, km: 3.0 },
      { c: "M02", d: "l", n: "Viroconium", r: "Roman city falling to ruin. Watling Street.", lat: 52.674, lon: -2.645, km: 3.0 },
      { c: "M03", d: "r", n: "The Wrekin", r: "Iron Age hillfort and the beacon.", lat: 52.668, lon: -2.552, km: 3.0 },
      { c: "M04", d: "r", n: "Wenlock Edge", r: "Limestone scarp, colliers and kilns.", lat: 52.570, lon: -2.620, km: 3.5 },
      { c: "M05", d: "b", n: "The Long Forest", r: "Coppice, oak standards, the white hart.", lat: 52.615, lon: -2.770, km: 3.5 },
      { c: "M06", d: "b", n: "The Long Mynd", r: "High moor, deep batches, the Portway.", lat: 52.540, lon: -2.840, km: 4.0 },
      { c: "M07", d: "t", n: "The Stiperstones", r: "Quartzite tors and Roman lead mines.", lat: 52.580, lon: -2.930, km: 3.5 },
      { c: "M08", d: "l", n: "The High Country", r: "Uld land. No roads.", lat: 52.560, lon: -3.020, km: 4.0 },
      { c: "M09", d: "r", n: "The Meres and Mosses", r: "Dark meres, carr and raised bog.", lat: 52.905, lon: -2.850, km: 4.0 },
      { c: "M10", d: "r", n: "The Clee Hills", r: "Brigand country. Abdon Burf.", lat: 52.490, lon: -2.595, km: 3.5 },
      { c: "M11", d: "x", n: "Salinae", r: "Salt town on the Salt Way.", lat: 52.267, lon: -2.150, km: 1.5 }
    ];
    var links = [["M01","M02"],["M01","M04"],["M01","M05"],["M02","M03"],["M02","M06"],["M04","M05"],
      ["M05","M06"],["M06","M07"],["M07","M08"],["M02","M09"],["M04","M10"],["M02","M11"]];
    var severn = [[52.660,-3.150],[52.735,-2.950],[52.712,-2.800],[52.708,-2.752],[52.688,-2.690],[52.672,-2.645],
      [52.633,-2.600],[52.628,-2.485],[52.533,-2.418],[52.376,-2.317],[52.270,-2.250],[52.190,-2.222]];
    var watling = [[52.674,-2.645],[52.680,-2.552],[52.690,-2.400],[52.700,-2.250],[52.705,-2.120]];
    var watlingW = [[52.674,-2.645],[52.600,-2.760],[52.538,-2.806],[52.460,-2.840]];
    var saltway = [[52.700,-2.250],[52.500,-2.170],[52.267,-2.150]];

    var lat0 = 52.6, kx = 111.32 * Math.cos(lat0 * Math.PI / 180), ky = 110.57;
    var minLon = -3.21, maxLon = -2.34, minLat = 52.43, maxLat = 52.96;
    var W = (maxLon - minLon) * kx, H = (maxLat - minLat) * ky; // km
    var S = 12; // px per km
    var VW = Math.round(W * S), VH = Math.round(H * S);
    function P(lat, lon) { return [((lon - minLon) * kx) * S, ((maxLat - lat) * ky) * S]; }
    function line(pts) { return pts.map(function (p, i) { var q = P(p[0], p[1]); return (i ? "L" : "M") + q[0].toFixed(1) + " " + q[1].toFixed(1); }).join(" "); }
    var byCode = {}; R.forEach(function (r) { byCode[r.c] = r; });

    var s = '<svg viewBox="0 0 ' + VW + " " + VH + '" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Map of the eleven region windows on the real Shropshire geography">';
    s += '<defs><clipPath id="frame"><rect x="14" y="14" width="' + (VW - 28) + '" height="' + (VH - 28) + '"/></clipPath><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><line x1="0" y1="0" x2="0" y2="8" stroke="#cdbf9f" stroke-width="1"/></pattern></defs>';
    s += '<rect width="' + VW + '" height="' + VH + '" fill="#e6dcc5"/>';
    s += '<rect x="8" y="8" width="' + (VW - 16) + '" height="' + (VH - 16) + '" fill="none" stroke="#1b1712" stroke-width="2"/>';
    s += '<rect x="14" y="14" width="' + (VW - 28) + '" height="' + (VH - 28) + '" fill="none" stroke="#1b1712" stroke-width="0.7"/>';
    // compass
    s += '<g transform="translate(' + (VW - 60) + ',64)" fill="#1b1712" font-family="Cinzel, Georgia, serif" font-size="14" text-anchor="middle"><path d="M0 -30 L7 0 L0 30 L-7 0 Z" fill="none" stroke="#1b1712"/><path d="M0 -30 L7 0 L-7 0 Z"/><text y="-36">N</text></g>';
    // routes
    s += '<g clip-path="url(#frame)">';
    s += '<g fill="none" stroke="#7a6a52" stroke-width="1.5" stroke-dasharray="1 5" stroke-linecap="round">';
    links.forEach(function (l) { if (l[1] === "M11") return; var a = byCode[l[0]], b = byCode[l[1]]; s += '<path d="' + line([[a.lat, a.lon], [b.lat, b.lon]]) + '"/>'; });
    s += "</g>";
    // roads
    s += '<g fill="none" stroke="#8b3a2a" stroke-width="2.2" stroke-dasharray="10 5">' +
      '<path d="' + line(watling) + '"/><path d="' + line(watlingW) + '"/><path d="' + line(saltway) + '" stroke-dasharray="3 5" stroke-width="1.6"/></g>';
    // river
    s += '<path d="' + line(severn) + '" fill="none" stroke="#5d7a86" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" opacity="0.85"/></g>';
    var sv = P(52.600, -2.440);
    s += '<text x="' + sv[0] + '" y="' + sv[1] + '" font-family="EB Garamond, Georgia, serif" font-style="italic" font-size="17" fill="#3f5862" transform="rotate(67 ' + sv[0] + " " + sv[1] + ')">Sabrina fl.</text>';
    var wl = P(52.703, -2.500);
    s += '<text x="' + wl[0] + '" y="' + wl[1] + '" font-family="EB Garamond, Georgia, serif" font-style="italic" font-size="15" fill="#8b3a2a">Watling Street</text>';
    // windows
    R.forEach(function (r) {
      var w = r.km * S, txt = "#1b1712", code = "#8b2e20";
      if (r.d === "x") { // off-map pointer (Salinae lies 45 miles south-east)
        var px = VW - 34, py = VH - 70;
        s += '<g class="map-node" data-code="' + r.c + '" tabindex="0">' +
          '<path d="M' + (px - 70) + " " + (py - 40) + " L" + (px - 6) + " " + (py + 8) + '" stroke="#8b3a2a" stroke-width="1.6" stroke-dasharray="3 5" fill="none"/>' +
          '<path d="M' + px + " " + (py + 12) + " l-12 -2 l7 -8 z" + '" fill="#8b3a2a"/>' +
          '<text x="' + px + '" y="' + (py + 32) + '" text-anchor="end" font-family="Cinzel, Georgia, serif" font-weight="700" font-size="14" fill="' + code + '">' + r.c + ' Salinae</text>' +
          '<text x="' + px + '" y="' + (py + 48) + '" text-anchor="end" font-family="EB Garamond, Georgia, serif" font-style="italic" font-size="14" fill="' + txt + '">45 miles by the Salt Way</text></g>';
        return;
      }
      var p = P(r.lat, r.lon), tx, ty, anchor;
      if (r.d === "l") { tx = p[0] - w / 2 - 8; ty = p[1] - 2; anchor = "end"; }
      else if (r.d === "t") { tx = p[0]; ty = p[1] - w / 2 - 22; anchor = "middle"; }
      else if (r.d === "b") { tx = p[0]; ty = p[1] + w / 2 + 16; anchor = "middle"; }
      else { tx = p[0] + w / 2 + 8; ty = p[1] - 2; anchor = "start"; }
      s += '<g class="map-node" data-code="' + r.c + '" tabindex="0">' +
        '<rect x="' + (p[0] - w / 2) + '" y="' + (p[1] - w / 2) + '" width="' + w + '" height="' + w + '" fill="url(#hatch)" stroke="#1b1712" stroke-width="1.2"/>' +
        '<circle class="dot" cx="' + p[0] + '" cy="' + p[1] + '" r="5" fill="#1b1712"/>' +
        '<text x="' + tx + '" y="' + ty + '" text-anchor="' + anchor + '" font-family="Cinzel, Georgia, serif" font-weight="700" font-size="14" fill="' + code + '">' + r.c + "</text>" +
        '<text x="' + tx + '" y="' + (ty + 16) + '" text-anchor="' + anchor + '" font-family="EB Garamond, Georgia, serif" font-size="15" fill="' + txt + '">' + r.n + "</text></g>";
    });
    // scale bar 10 km
    s += '<g transform="translate(36,' + (VH - 40) + ')" font-family="Inter, sans-serif" font-size="11" fill="#1b1712"><rect width="' + (10 * S) + '" height="5" fill="#1b1712"/><rect x="' + (5 * S) + '" width="' + (5 * S) + '" height="5" fill="#e6dcc5" stroke="#1b1712"/><text y="-6">0</text><text x="' + (10 * S) + '" y="-6" text-anchor="middle">10 km</text></g>';
    s += "</svg>";
    el.innerHTML = s;

    var list = document.getElementById("region-list");
    if (list) {
      list.innerHTML = R.map(function (r) {
        return '<li data-code="' + r.c + '"><span class="code">' + r.c + '</span><span><span class="name">' + r.n +
          '</span><br><span class="role">' + r.r + " " + r.km.toFixed(1) + " km window.</span></span></li>";
      }).join("");
    }
    function setActive(code) {
      document.querySelectorAll("[data-code]").forEach(function (n) {
        n.classList.toggle("active", n.getAttribute("data-code") === code);
      });
    }
    document.querySelectorAll("[data-code]").forEach(function (n) {
      n.addEventListener("mouseenter", function () { setActive(n.getAttribute("data-code")); });
      n.addEventListener("focus", function () { setActive(n.getAttribute("data-code")); });
      n.addEventListener("mouseleave", function () { setActive(null); });
    });
  }
})();
