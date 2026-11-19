/* =====================================================================
 * 코드 복사 버튼 — <pre data-copy>마다 오른쪽 위에 복사 아이콘을 단다
 *
 * - 누르면 코드 글자 그대로(줄바꿈 포함) 클립보드에 넣고, 1.5초 동안 체크 표시.
 * - 페이지 원본에는 data-copy 표시만 있고, 버튼은 여기서 만든다.
 * ===================================================================== */
(function () {
  var COPY = '<svg class="cp-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/>' +
    '<path d="M5 15H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v1"/></svg>';
  var DONE = '<svg class="cp-done" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';

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

  function attach(pre) {
    var text = pre.innerText.replace(/\n+$/, '');       // 버튼을 달기 전에 코드 글자만 읽어 둔다
    var wrap = document.createElement('div');
    wrap.className = 'cp-wrap';
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'cp-btn';
    btn.setAttribute('aria-label', '코드 복사');
    btn.title = '복사';
    btn.innerHTML = COPY + DONE;
    wrap.appendChild(btn);

    var timer;
    btn.addEventListener('click', function () {
      copyText(text).then(function () {
        btn.classList.add('done');
        btn.setAttribute('aria-label', '복사됨');
        clearTimeout(timer);
        timer = setTimeout(function () {
          btn.classList.remove('done');
          btn.setAttribute('aria-label', '코드 복사');
        }, 1500);
      });
    });
  }

  var pres = document.querySelectorAll('pre[data-copy]');
  for (var i = 0; i < pres.length; i++) attach(pres[i]);
})();
