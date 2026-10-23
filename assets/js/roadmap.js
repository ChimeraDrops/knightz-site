/* RoadMap: filters, search and image lightbox */
(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll('.rm-item, .rm-tile'));
  var filter = 'all', q = '';
  function apply() {
    var shown = 0;
    items.forEach(function (el) {
      var ok = (filter === 'all' || el.getAttribute('data-state') === filter) && (!q || el.getAttribute('data-name').indexOf(q) !== -1 || el.textContent.toLowerCase().indexOf(q) !== -1);
      if (ok) { el.removeAttribute('data-hidden'); shown++; } else el.setAttribute('data-hidden', '');
    });
    document.querySelectorAll('.rm-group').forEach(function (g) {
      var any = g.querySelector('.rm-item:not([data-hidden]), .rm-tile:not([data-hidden])');
      if (any) g.removeAttribute('data-hidden'); else g.setAttribute('data-hidden', '');
    });
    var e = document.querySelector('.rm-empty'); if (e) e.hidden = shown !== 0;
  }
  document.querySelectorAll('.rm-filters button').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.rm-filters button').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on'); filter = b.getAttribute('data-f'); apply();
    });
  });
  var s = document.querySelector('.rm-search');
  if (s) s.addEventListener('input', function () { q = s.value.trim().toLowerCase(); apply(); });

  // Lightbox
  var links = function () { return Array.prototype.slice.call(document.querySelectorAll('a[data-lb]')).filter(function (a) { return !a.closest('[data-hidden]'); }); };
  if (!document.querySelector('a[data-lb]')) return;
  var lb = document.createElement('div');
  lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Image viewer');
  lb.innerHTML = '<span class="lb-count"></span><button type="button" class="lb-x" aria-label="Close">&times;</button><button type="button" class="lb-p" aria-label="Previous image">&lsaquo;</button><button type="button" class="lb-n" aria-label="Next image">&rsaquo;</button><figure style="margin:0;display:flex;flex-direction:column;align-items:center;max-width:100%"><img alt=""><figcaption></figcaption></figure><a class="lb-o" target="_blank" rel="noopener">Open full size image</a>';
  document.body.appendChild(lb);
  var img = lb.querySelector('img'), cap = lb.querySelector('figcaption'), cnt = lb.querySelector('.lb-count'), open = lb.querySelector('.lb-o');
  var list = [], idx = 0, last = null;
  function show(i) {
    idx = (i + list.length) % list.length;
    var a = list[idx];
    img.src = a.getAttribute('href'); img.alt = a.getAttribute('data-lb');
    cap.textContent = a.getAttribute('data-lb'); open.href = a.getAttribute('href');
    cnt.textContent = (idx + 1) + ' / ' + list.length;
  }
  function close() { lb.classList.remove('open'); document.body.style.overflow = ''; img.src = ''; if (last) last.focus(); }
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[data-lb]');
    if (!a || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault(); last = a; list = links(); show(list.indexOf(a));
    lb.classList.add('open'); document.body.style.overflow = 'hidden'; lb.querySelector('.lb-x').focus();
  });
  lb.querySelector('.lb-x').addEventListener('click', close);
  lb.querySelector('.lb-p').addEventListener('click', function () { show(idx - 1); });
  lb.querySelector('.lb-n').addEventListener('click', function () { show(idx + 1); });
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close(); else if (e.key === 'ArrowLeft') show(idx - 1); else if (e.key === 'ArrowRight') show(idx + 1);
  });
})();
