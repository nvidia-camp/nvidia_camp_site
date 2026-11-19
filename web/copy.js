/* =====================================================================
 * 코드 복사 아이콘 — 모든 페이지의 코드 칸에 같은 모양으로
 *
 * 두 가지 칸에 단다 (빌드가 표시를 붙인다, sitebuild/nav.py):
 *   <pre data-copy>  이 사이트가 단 칸. 누르면 칸의 글자를 그대로 복사한다.
 *   <pre data-cp=N>  페이지에 원래 '코드 복사' 글자 버튼이 있던 칸. 원래 버튼(data-cp-src=N)은 숨기고,
 *                    아이콘을 누르면 그 버튼을 대신 눌러 페이지의 원래 복사 방식을 그대로 쓴다
 *                    (줄 번호 빼기, PowerShell·Bash 전환 등).
 * - 누르면 1.5초 동안 체크 표시.
 * - 아이콘 색은 그 칸의 글자색을 따른다 (어두운 칸·밝은 칸, 화면 밝기 전환 모두).
 * ===================================================================== */
(function () {
  var COPY = '<svg class="cp-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/>' +
    '<path d="M5 15H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v1"/></svg>';
  var DONE = '<svg class="cp-done" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';
  var pairs = [];   // [칸, 아이콘 버튼]

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {      // 옛 브라우저·http 주소용
      var area = document.createElement('textarea');
      area.value = text;
      area.setAttribute('readonly', '');
      area.style.position = 'fixed';
      area.style.opacity = '0';
      document.body.appendChild(area);
      area.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) {}
      document.body.removeChild(area);
      if (ok) resolve(); else reject();
    });
  }

  function paint(pre, btn) { btn.style.color = getComputedStyle(pre).color; }

  function attach(pre) {
    // 칸을 감싸 오른쪽 위에 아이콘을 둔다. 칸의 바깥 여백은 감싸개로 옮겨 아이콘이 칸 안에 오게 한다.
    var cs = getComputedStyle(pre);
    var wrap = document.createElement('div');
    wrap.className = 'cp-wrap';
    wrap.style.margin = cs.marginTop + ' ' + cs.marginRight + ' ' + cs.marginBottom + ' ' + cs.marginLeft;
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);
    pre.style.margin = '0';

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'cp-btn';
    btn.setAttribute('aria-label', '코드 복사');
    btn.title = '복사';
    btn.innerHTML = COPY + DONE;
    wrap.appendChild(btn);
    paint(pre, btn);
    pairs.push([pre, btn]);

    var id = pre.getAttribute('data-cp');
    var original = id && document.querySelector('[data-cp-src="' + id + '"]');
    var timer;
    function done() {
      btn.classList.add('done');
      btn.setAttribute('aria-label', '복사됨');
      clearTimeout(timer);
      timer = setTimeout(function () {
        btn.classList.remove('done');
        btn.setAttribute('aria-label', '코드 복사');
      }, 1500);
    }
    btn.addEventListener('click', function () {
      if (original) { original.click(); done(); return; }      // 페이지 원래 복사 방식
      copyText(pre.innerText.replace(/\n+$/, '')).then(done);   // 누를 때의 글자 (전환된 명령도 그대로)
    });
  }

  var pres = document.querySelectorAll('pre[data-copy], pre[data-cp]');
  for (var i = 0; i < pres.length; i++) attach(pres[i]);

  // 화면 밝기를 바꾸면 칸 글자색이 바뀌므로 아이콘 색도 다시 맞춘다
  function repaint() { for (var j = 0; j < pairs.length; j++) paint(pairs[j][0], pairs[j][1]); }
  if (window.MutationObserver) new MutationObserver(repaint).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme', 'style'] });
  var os = window.matchMedia && matchMedia('(prefers-color-scheme: dark)');
  if (os && os.addEventListener) os.addEventListener('change', function () { setTimeout(repaint, 0); });
})();
