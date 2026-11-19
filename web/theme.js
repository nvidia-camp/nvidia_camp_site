/* =====================================================================
 * 라이트/다크 전환 — 화면 밝기 버튼(.theme-toggle)
 *
 * build_site.py가 다크 CSS가 있는 페이지의 <head>에 이 파일을 끼워 넣는다.
 * (홈·과목 목록은 항상, 요약·가이드는 원본에 prefers-color-scheme가 있을 때만)
 *
 * 원리
 *   페이지마다 어두운 화면용 CSS가 @media (prefers-color-scheme: dark) { … } 안에 있다.
 *   원래는 컴퓨터(OS) 설정을 따라 켜지고 꺼진다. 버튼을 누르면 그 media 조건 글자를
 *     다크 고정 → (min-width:0px)                     항상 참
 *     라이트 고정 → (max-width:0px) and (min-width:1px)  항상 거짓
 *   으로 바꿔 끼워, OS 설정과 관계없이 고른 쪽을 보여 준다.
 *
 * 저장
 *   고른 값은 localStorage 'site-theme'에 둔다 (다른 페이지·새로고침에도 유지).
 *   OS 설정과 같은 쪽을 고르면 저장값을 지워 다시 OS 설정을 따른다.
 *
 * 번쩍임 막기
 *   페이지를 읽는 도중에 추가되는 <style>(강의 목차 블록 등)도 화면에 그려지기 전에
 *   바꿔 끼우도록, 읽기가 끝날 때(DOMContentLoaded)까지 새 style·link를 지켜본다.
 * ===================================================================== */
(function () {

  /* ── 1. 설정 ──────────────────────────────────────────────────────── */
  var STORAGE_KEY = 'site-theme';
  var DARK_QUERY = /\(\s*prefers-color-scheme\s*:\s*dark\s*\)/i;   // 바꿔 끼울 media 조건
  var ALWAYS = '(min-width:0px)';                                  // 항상 참
  var NEVER = '(max-width:0px) and (min-width:1px)';               // 항상 거짓

  var doc = document;
  var root = doc.documentElement;
  var osDark = matchMedia('(prefers-color-scheme: dark)');         // OS 설정

  var seenSheets = [];   // 이미 훑어본 스타일시트
  var darkRules = [];    // [규칙, 원래 media 글자] — 바꿔 끼울 대상
  var memory = '';       // localStorage를 못 쓰는 브라우저(사생활 보호 모드 등)용 임시 저장


  /* ── 2. 고른 값 읽기·저장: 'dark' · 'light' · ''(OS 설정 따름) ────── */
  function getChoice() {
    try {
      var v = localStorage.getItem(STORAGE_KEY);
      return v === 'dark' || v === 'light' ? v : '';
    } catch (e) {
      return memory;
    }
  }

  function saveChoice(v) {
    memory = v;
    try {
      if (v) localStorage.setItem(STORAGE_KEY, v);
      else localStorage.removeItem(STORAGE_KEY);
    } catch (e) {}
  }

  function osMode() {
    return osDark.matches ? 'dark' : 'light';
  }


  /* ── 3. 다크 CSS 규칙 찾기 ──────────────────────────────────────────
   *   스타일시트 안에서 media 조건에 prefers-color-scheme: dark가 있는 규칙을
   *   모두 모은다. @media 안의 @media처럼 겹친 규칙도 따라 들어간다.        */
  function collectDarkRules(rules) {
    for (var i = 0; i < rules.length; i++) {
      var rule = rules[i];
      if (rule.media && DARK_QUERY.test(rule.media.mediaText)) {
        darkRules.push([rule, rule.media.mediaText]);
      }
      if (rule.cssRules) collectDarkRules(rule.cssRules);
    }
  }

  function scanNewSheets() {
    var sheets = doc.styleSheets;
    for (var i = 0; i < sheets.length; i++) {
      var sheet = sheets[i];
      if (seenSheets.indexOf(sheet) >= 0) continue;
      seenSheets.push(sheet);
      try { collectDarkRules(sheet.cssRules); } catch (e) {}   // 다른 도메인 CSS는 읽을 수 없다
    }
  }


  /* ── 4. 화면에 적용 ─────────────────────────────────────────────── */
  function apply() {
    scanNewSheets();
    var choice = getChoice();
    var mode = choice || osMode();   // 지금 보여 줄 쪽

    // 다크 CSS 규칙의 media 조건 바꿔 끼우기 (고른 값이 없으면 원래대로)
    for (var j = 0; j < darkRules.length; j++) {
      var rule = darkRules[j][0], original = darkRules[j][1];
      rule.media.mediaText = choice
        ? original.replace(DARK_QUERY, choice === 'dark' ? ALWAYS : NEVER)
        : original;
    }

    // 버튼 아이콘(해·달)과 브라우저 기본 색(스크롤바·입력창)
    root.setAttribute('data-theme', mode);
    root.style.colorScheme = choice;

    // 버튼 설명: 누르면 무엇이 되는지
    var label = mode === 'dark' ? '밝은 화면으로 보기' : '어두운 화면으로 보기';
    var buttons = doc.querySelectorAll('.theme-toggle');
    for (var k = 0; k < buttons.length; k++) {
      buttons[k].setAttribute('aria-label', label);
      buttons[k].setAttribute('data-tip', label);
    }
  }


  /* ── 5. 버튼 누름: 지금과 반대쪽으로 ──────────────────────────────── */
  doc.addEventListener('click', function (e) {
    var button = e.target.closest && e.target.closest('.theme-toggle');
    if (!button) return;
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    saveChoice(next === osMode() ? '' : next);   // OS 설정과 같으면 저장값을 지운다
    apply();
  });


  /* ── 6. OS 설정이 바뀌면 다시 적용 ────────────────────────────────── */
  if (osDark.addEventListener) osDark.addEventListener('change', apply);
  else osDark.addListener(apply);   // 옛 Safari


  /* ── 7. 시작: 지금 한 번, 읽는 도중 새 CSS가 생길 때마다, 다 읽은 뒤 한 번 ── */
  apply();

  var watcher = window.MutationObserver && new MutationObserver(function (changes) {
    for (var i = 0; i < changes.length; i++) {
      for (var j = 0; j < changes[i].addedNodes.length; j++) {
        var name = changes[i].addedNodes[j].nodeName;
        if (name === 'STYLE' || name === 'LINK') { apply(); return; }
      }
    }
  });
  if (watcher) watcher.observe(root, { childList: true, subtree: true });

  doc.addEventListener('DOMContentLoaded', function () {
    if (watcher) watcher.disconnect();
    apply();
  });
})();
