"""Day25 3번 탭 'Basic 완주 안내' 만들기.

원본: nvidia_camp/05_LLM_RAG/20261120/안내서.html (강사님 자료, 읽기만 한다)
결과: 이 폴더의 index.html

본문 글자는 한 글자도 바꾸지 않는다. 바꾸는 것은 아래뿐이다.
  1. 원본 목차 <nav>에 class="toc"를 붙이고 CSS의 nav 규칙을 nav.toc로 좁힌다
     (사이트 위쪽 메뉴 nav.cn-nav에 원본 규칙이 걸리지 않게)
  2. 머리말 아래에 Day25 탭 줄(1 사전 준비 · 2 요구사항 명세서 · 3 Basic 완주 안내)을 넣는다
  3. 다크 모드 CSS와 접힌 코드(<details>)를 눈에 띄게 하는 CSS를 덧붙인다
  4. 작성자 개인 ChatGPT 라이브러리 링크 3개는 <a>만 벗겨 글자로 남긴다 (학생은 열 수 없는 주소)
  6. 머리말을 1·2번 탭과 같은 크기로 맞추고, 부제 두 줄(<br>)을 ' · '로 이어 한 줄로 만든다 (사용자 승인)
  7. 체크 진행 패널(1100px 이상 오른쪽 고정 — 1652px 미만은 본문 오른쪽을 줄여 자리 확보, 더 좁으면 오른쪽 아래 버튼) + 전체 지우기. 체크 값은 원본 localStorage 그대로
  5. 위쪽 고정 목차에 지금 보는 절 표시(scrollspy) CSS·JS를 덧붙인다. 휴대폰에서는 한 줄 가로 띠로 고정

실행: python3 make_page.py
"""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[4] / "05_LLM_RAG" / "20261120" / "안내서.html"
OUT = HERE / "index.html"


def replace_once(text: str, old: str, new: str) -> str:
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"'{old[:60]}' 이(가) {n}번 나옴 (1번이어야 함). 원본이 바뀌었는지 확인하세요.")
    return text.replace(old, new)


TABS_CSS = """
:root{--tab-bg:#ffffff;--tab-border:#cbd7e3;--tab-fg:#162237;--tab-n-bg:#e7eef6;--tab-n-fg:#172d49;
  --tab-act-bg:#172d49;--tab-act-fg:#ffffff;--tab-lec-bg:#eef6ff;--tab-lec-border:#b8d0e9;--tab-lec-fg:#124d8a}
.tabs-wrap{max-width:1220px;margin:18px auto 20px;padding:0 20px}
main{margin-top:20px}
@media(max-width:720px){.tabs-wrap{margin-bottom:12px}main{margin-top:16px}}
nav.toc{padding-left:max(20px,calc((100% - 1180px)/2));padding-right:max(20px,calc((100% - 1180px)/2))}
.code-tools{display:none}
@media(max-width:500px){.file-card{padding:14px 12px}.file-card details{padding:0 10px}
  pre,pre code{white-space:pre;overflow-wrap:normal;word-break:normal}pre{overflow-x:auto}
  .cp-wrap>pre{padding-right:14px;padding-top:46px}}
.tabs{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.tabs a{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:6px 15px 6px 8px;border:1px solid var(--tab-border);border-radius:999px;background:var(--tab-bg);color:var(--tab-fg);text-decoration:none;font-size:15px;font-weight:650;line-height:1.75}
.tabs a:hover{border-color:#205a9c;color:var(--tab-fg)}
.tabs .n{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:999px;background:var(--tab-n-bg);color:var(--tab-n-fg);font-size:13px;font-weight:700}
.tabs a[aria-current='page']{background:var(--tab-act-bg);border-color:var(--tab-act-bg);color:var(--tab-act-fg)}
.tabs a[aria-current='page'] .n{background:var(--tab-act-fg);color:var(--tab-act-bg)}
.tabs a.lec{margin-left:auto;padding:6px 14px;background:var(--tab-lec-bg);border-color:var(--tab-lec-border);color:var(--tab-lec-fg)}
@media(max-width:720px){.tabs-wrap{padding:0 16px}.tabs a.lec{margin-left:0}}
@media print{.tabs-wrap{display:none}}
"""

# 머리말: 1·2번 탭과 같은 크기·색 (탭을 바꿔도 배너·탭 줄이 움직이지 않고 글자만 바뀌게)
HEADER_CSS = """
header{background:linear-gradient(110deg,#172d49,#1d3a5f);color:#fff;padding:34px max(30px,calc((100% - 1180px)/2));border-bottom:1px solid #2d4863;line-height:1.75}
header .eyebrow{color:#c9ddf3;font-size:13px;font-weight:700;letter-spacing:.12em;line-height:1.75}
header h1{color:#fff;margin:.4rem 0;font-size:33px;line-height:1.75;letter-spacing:normal}
header p,header p.lead{max-width:1000px;color:#dce8f5;margin:0;font-size:15px;line-height:1.75}
@media(max-width:720px){header{padding:25px 20px}header h1{font-size:26px}}
/* 탭을 바꿔도 머리말 높이가 같게: 부제 자리를 가장 긴 탭(3번) 기준 줄 수만큼 잡아 둔다 */
@media(max-width:960px){header p:not(.eyebrow){min-height:calc(2 * 1.75em)}}
@media(max-width:480px){header p:not(.eyebrow){min-height:calc(3 * 1.75em)}}
"""

# 접힌 전체 코드: 눌러서 펼치는 칸이라는 것이 보이게 (글자는 원본 그대로)
FOLD_CSS = """
.file-card details{border-color:#b8cbe2;border-left:4px solid #214e84;background:#f5f8fc}
.file-card details>summary{list-style:none;display:flex;align-items:center;gap:10px}
.file-card details>summary::-webkit-details-marker{display:none}
.file-card details>summary::before{content:"";flex:none;width:9px;height:9px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(-45deg);transition:transform .15s;margin:0 3px}
.file-card details[open]>summary::before{transform:rotate(45deg)}
.file-card details[open]{background:#fbfcfe}
"""

DARK_CSS = """
@media (prefers-color-scheme:dark){
:root{color-scheme:dark;--ink:#e5eaf2;--sub:#9ab6d4;--blue:#93c5fd;--teal:#7fd3c4;--border:#29384e;--paper:#102137;--wash:#0b1220;--soft:#132a44;--warn:#f3c98b;--warn-bg:#2b2112;
  --tab-bg:#102137;--tab-border:#35536d;--tab-fg:#e5eaf2;--tab-n-bg:#1c3554;--tab-n-fg:#93c5fd;
  --tab-act-bg:#93c5fd;--tab-act-fg:#0b1220;--tab-lec-bg:#132c45;--tab-lec-border:#3b6182;--tab-lec-fg:#b4d9f5}
a{color:#93c5fd}a:hover{color:#bfdbfe}
header{background:linear-gradient(110deg,#0f2139,#132c45);border-bottom:1px solid #2d4863}header .eyebrow{color:#95b9d5}header p,header p.lead{color:#bcd1e0}
.meta span{background:#1c3554;border-color:#3b6182}
nav.toc{background:#102137;border-bottom-color:#29384e;box-shadow:0 3px 12px #00000040}
section{box-shadow:none}
.legend span{background:#12302c;color:#bfe7de;border-color:#2c5a52}
blockquote{background:#10292a;color:#cdeee6}blockquote span{color:#8fd3c3}
.note{background:#112438;border-color:#2d4863}.note strong{color:#b4d9f5}
.attention{border-color:#6b5224}.attention strong{color:#f3c98b}
.gate{background:#10292a;color:#a8e3d6;border-top-color:#2c5a52}
th,td{border-right-color:#29384e;border-bottom-color:#29384e}th{background:#17304a;color:#e3f4ff}tbody tr:nth-child(even){background:#0f1e31}
code{background:#172940;color:#9fe4d1}
pre{background:#091321;color:#ccdfef;border-color:#2c4560}pre:before{color:#7fb3e0}
details{background:#0f1e31;border-color:#2d4863}summary{color:#b4d9f5}details[open] summary{border-bottom-color:#29384e}
.todo{border-top-color:#29384e}.todo .tag{color:#7fd3c4}.todo details{background:#0f1e31}
.file-card{background:#102137;border-color:#35536d}.file-meta,.small,.copy-status{color:#9ab6d4}.replace{color:#f3c98b}
.copy-button{background:#93c5fd;border-color:#93c5fd;color:#0b1220}.copy-button:hover{background:#bfdbfe}
.checkline{background:#10292a;border-color:#2c5a52}.checkline input{accent-color:#7fd3c4}.phase-status{color:#a8e3d6}
.request-card{border-top-color:#2d4863}.request-card .request-no{color:#7fd3c4}
.manual{background:#2b2112;border-color:#6b5224}
.empty-file{background:#0f1e31;border-color:#3b6182}
.file-card details{background:#0d1b2c;border-color:#3b6182;border-left-color:#93c5fd}.file-card details[open]{background:#0f1e31}
}
"""

# 위쪽 고정 목차에 '지금 보는 절' 표시 (scrollspy). 휴대폰에서는 한 줄 가로 스크롤 띠로 고정
SPY_CSS = """
nav.toc{top:var(--cn-h,48px);gap:2px;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none}
nav.toc::-webkit-scrollbar{display:none}
nav.toc{padding-top:8px;padding-bottom:8px;border-bottom:0;box-shadow:0 1px 0 #d6dfec}
nav.toc a{flex:none;padding:4.75px 8px;border-radius:999px;line-height:1.5;white-space:nowrap;transition:background-color .25s,color .25s,box-shadow .25s}
nav.toc a:hover{text-decoration:none;background:#eaf1fa}
nav.toc a.on{background:#214e84;color:#fff;box-shadow:0 2px 8px #214e8433}
@media(max-width:1240px){
  nav.toc{-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 16px,#000 calc(100% - 28px),transparent);
                  mask-image:linear-gradient(90deg,transparent 0,#000 16px,#000 calc(100% - 28px),transparent)}
}
@media(max-width:850px){nav.toc{position:sticky;-webkit-overflow-scrolling:touch;padding:8px 16px}}
@media (prefers-color-scheme:dark){
  nav.toc{box-shadow:0 1px 0 #29384e}
  nav.toc a:hover{background:#17304a}
  nav.toc a.on{background:#93c5fd;color:#0b1220;box-shadow:0 2px 10px #93c5fd33}
}
"""

SPY_JS = """<script>
(() => {
  const toc = document.querySelector('nav.toc');
  if (!toc) return;
  const links = [...toc.querySelectorAll('a[href^="#"]')];
  const items = links.map(a => [a, document.getElementById(a.getAttribute('href').slice(1))]).filter(x => x[1]);
  const root = document.documentElement;
  let cur = null, ticking = false;

  // 사이트 위쪽 메뉴 높이에 맞춰 목차를 붙이고, 목차로 이동할 때 제목이 가리지 않게 한다
  function measure() {
    const bar = document.querySelector('.cn-nav');
    const h = bar ? bar.getBoundingClientRect().height : 0;
    root.style.setProperty('--cn-h', h + 'px');
    root.style.scrollPaddingTop = (h + toc.getBoundingClientRect().height + 16) + 'px';
  }

  function update() {
    ticking = false;
    const line = toc.getBoundingClientRect().bottom + 40;
    let on = items[0];
    for (const it of items) { if (it[1].getBoundingClientRect().top <= line) on = it; else break; }
    if (innerHeight + scrollY >= root.scrollHeight - 4) on = items[items.length - 1];
    if (on[0] === cur) return;
    if (cur) { cur.classList.remove('on'); cur.removeAttribute('aria-current'); }
    cur = on[0];
    cur.classList.add('on');
    cur.setAttribute('aria-current', 'location');
    if (toc.scrollWidth > toc.clientWidth + 2) {   // 한 줄 띠일 때 지금 절을 가운데로
      toc.scrollTo({ left: cur.offsetLeft - (toc.clientWidth - cur.offsetWidth) / 2, behavior: 'smooth' });
    }
  }
  const request = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };

  measure(); update();
  addEventListener('scroll', request, { passive: true });
  addEventListener('resize', () => { measure(); request(); });
  addEventListener('load', () => { measure(); request(); });
})();
</script>"""

# 체크 진행 패널: 1652px 이상은 오른쪽 빈 여백에, 1100~1651px은 본문 오른쪽을 216px 줄여 만든 자리에 고정.
# 1100px 미만(화면 반 나누기·태블릿·휴대폰)은 오른쪽 아래 '17/48' 버튼을 눌러 펼친다.
# 체크 값은 원본 스크립트가 쓰는 localStorage를 그대로 쓴다 (학생 브라우저에만 저장).
PROGRESS_CSS = """
.pg{position:fixed;z-index:850;width:204px;box-sizing:border-box;padding:14px 14px 12px;border:1px solid var(--border);border-radius:12px;
  background:var(--paper);color:var(--ink);box-shadow:0 6px 22px #0f1e3114;font-size:13px;line-height:1.5}
.pg-head{display:flex;align-items:baseline;justify-content:space-between;gap:8px;margin-bottom:8px}
.pg-head b{font-size:13px}
.pg-num{font-size:13px;font-weight:700;color:var(--blue);font-variant-numeric:tabular-nums}
.pg-bar{height:6px;border-radius:99px;background:var(--soft);overflow:hidden;margin-bottom:12px}
.pg-bar span{display:block;height:100%;width:0;border-radius:99px;background:var(--teal);transition:width .3s}
.pg-g{margin:0 0 10px}
.pg-g-h{display:flex;justify-content:space-between;font-size:12px;color:var(--sub);margin-bottom:4px}
.pg-g-h span{font-variant-numeric:tabular-nums}
.pg-cells{display:grid;grid-template-columns:repeat(16,1fr);gap:2px}
.pg-cell{aspect-ratio:1;min-width:0;padding:0;margin:0;border:1px solid var(--border);border-radius:3px;background:transparent;cursor:pointer}
.pg-cell:hover{border-color:var(--blue)}
.pg-cell.on{background:var(--teal);border-color:var(--teal)}
.pg-cell:focus-visible{outline:2px solid var(--blue);outline-offset:1px}
.pg-next{display:block;width:100%;margin:12px 0 0;padding:8px 10px;border:0;border-radius:8px;background:var(--soft);color:var(--blue);
  font:inherit;font-size:12px;text-align:left;cursor:pointer}
.pg-next b{display:block;font-size:13px;color:var(--ink)}
.pg-next:hover{filter:brightness(.97)}
.pg-next[disabled]{cursor:default;color:var(--teal)}
.pg-clear{margin-top:10px;padding-top:8px;border-top:1px solid var(--border);font-size:12px;color:var(--sub)}
.pg-clear button{padding:2px 0;border:0;background:none;color:var(--sub);font:inherit;text-decoration:underline;text-underline-offset:2px;cursor:pointer}
.pg-clear button[disabled]{opacity:.45;cursor:default}
.pg-clear .pg-yes{color:#b42318;font-weight:700;margin-left:6px}.pg-clear .pg-no{margin-left:8px}
.checkline.pg-flash{animation:pgFlash 1.4s ease}
@keyframes pgFlash{0%,40%{box-shadow:0 0 0 3px var(--blue)}100%{box-shadow:0 0 0 0 transparent}}
.pg-chip{position:fixed;right:80px;bottom:28px;z-index:900;height:36px;padding:0 13px;border:1px solid var(--border);border-radius:999px;
  background:var(--paper);color:var(--ink);font:700 13px/1 "Malgun Gothic","Apple SD Gothic Neo",system-ui,sans-serif;
  box-shadow:0 4px 14px #0f1e3129;cursor:pointer;display:none;align-items:center;gap:7px;font-variant-numeric:tabular-nums}
.pg-chip i{display:block;width:8px;height:8px;border-radius:99px;background:var(--teal)}
@media(max-width:1099px){
  .pg-chip{display:inline-flex}
  .pg{right:16px;bottom:76px;width:min(300px,calc(100vw - 32px));display:none}
  .pg.open{display:block}
}
@media(min-width:1652px){.pg{right:max(16px,calc((100vw - 1180px)/2 - 220px))}}
/* 노트북 폭: 본문 왼쪽 끝은 그대로 두고 오른쪽만 줄여 패널 자리를 만든다 (머리말·탭 줄·목차 띠는 그대로) */
@media(min-width:1100px) and (max-width:1651px){main{margin-left:max(0px,calc((100% - 1220px)/2));margin-right:216px}.pg{right:16px}}
@media (prefers-color-scheme:dark){.pg,.pg-chip{box-shadow:0 6px 22px #00000066}.pg-clear .pg-yes{color:#fda29b}}
@media print{.pg,.pg-chip{display:none!important}}
"""

PROGRESS_JS = """<script>
(() => {
  const inputs = [...document.querySelectorAll('input[data-check]')];
  if (!inputs.length) return;
  const tocText = id => (document.querySelector('nav.toc a[href="#' + id + '"]') || {}).textContent || '';
  const groups = [
    { key: 'step', label: '단계 01–10', items: [] },
    { key: 'postman', label: 'Postman 요청', items: [] },
    { key: 'finish', label: '완료 기준', items: [] },
  ];
  inputs.forEach(input => {
    const sec = input.closest('section');
    const id = sec ? sec.id : '';
    const g = id === 'postman' ? groups[1] : id === 'finish' ? groups[2] : groups[0];
    const text = (input.closest('.checkline') || input.parentElement).textContent.trim();
    const name = g.key === 'step' ? tocText(id) : g.key === 'postman' ? text.split(' — ')[0] : tocText(id) + ' · ' + text;
    g.items.push({ input, name });
  });
  const all = groups.flatMap(g => g.items);

  const panel = document.createElement('aside');
  panel.className = 'pg';
  panel.setAttribute('aria-label', '체크 진행 상황');
  panel.innerHTML = '<div class="pg-head"><b>진행 상황</b><span class="pg-num"></span></div><div class="pg-bar"><span></span></div>' +
    groups.map(g => '<div class="pg-g"><div class="pg-g-h">' + g.label + '<span></span></div><div class="pg-cells"></div></div>').join('') +
    '<button type="button" class="pg-next"></button><div class="pg-clear"></div>';
  const chip = document.createElement('button');
  chip.type = 'button';
  chip.className = 'pg-chip';
  chip.setAttribute('aria-expanded', 'false');
  chip.innerHTML = '<i></i><span></span>';
  document.body.append(panel, chip);

  const groupEls = [...panel.querySelectorAll('.pg-g')];
  groups.forEach((g, gi) => {
    const box = groupEls[gi].querySelector('.pg-cells');
    g.items.forEach(item => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'pg-cell';
      b.title = item.name;
      b.addEventListener('click', () => go(item));
      item.cell = b;
      box.append(b);
    });
  });
  const narrow = matchMedia('(max-width:1099px)');

  function go(item) {
    const line = item.input.closest('.checkline') || item.input;
    line.scrollIntoView({ behavior: 'smooth', block: 'center' });
    line.classList.remove('pg-flash'); void line.offsetWidth; line.classList.add('pg-flash');
    if (narrow.matches) toggle(false);
  }

  let confirming = false;
  function update() {
    const done = all.filter(i => i.input.checked).length;
    panel.querySelector('.pg-num').textContent = done + ' / ' + all.length;
    panel.querySelector('.pg-bar span').style.width = (100 * done / all.length) + '%';
    chip.querySelector('span').textContent = done + '/' + all.length;
    chip.setAttribute('aria-label', '체크 진행 상황 ' + done + '/' + all.length);
    groups.forEach((g, gi) => {
      groupEls[gi].querySelector('.pg-g-h span').textContent = g.items.filter(i => i.input.checked).length + '/' + g.items.length;
      g.items.forEach(i => { i.cell.classList.toggle('on', i.input.checked); i.cell.setAttribute('aria-label', i.name + (i.input.checked ? ' · 완료' : ' · 남음')); });
    });
    const next = all.find(i => !i.input.checked);
    const nb = panel.querySelector('.pg-next');
    nb.disabled = !next;
    nb.innerHTML = next ? '다음 할 일 →<b></b>' : '<b>모두 체크했어요</b>';
    if (next) nb.querySelector('b').textContent = next.name;
    nb.onclick = next ? () => go(next) : null;
    const clear = panel.querySelector('.pg-clear');
    if (confirming && done) {
      clear.innerHTML = '체크 ' + done + '개를 지울까요?<button type="button" class="pg-yes">지우기</button><button type="button" class="pg-no">취소</button>';
      clear.querySelector('.pg-yes').onclick = () => {
        confirming = false;
        all.forEach(i => { if (i.input.checked) { i.input.checked = false; i.input.dispatchEvent(new Event('change', { bubbles: true })); } });
        update();
      };
      clear.querySelector('.pg-no').onclick = () => { confirming = false; update(); };
    } else {
      confirming = false;
      clear.innerHTML = '<button type="button">전체 지우기</button>';
      const b = clear.querySelector('button');
      b.disabled = !done;
      b.onclick = () => { confirming = true; update(); };
    }
  }

  function toggle(open) {
    panel.classList.toggle('open', open);
    chip.setAttribute('aria-expanded', String(open));
  }
  chip.addEventListener('click', e => { e.stopPropagation(); toggle(!panel.classList.contains('open')); });
  document.addEventListener('click', e => { if (narrow.matches && panel.classList.contains('open') && !panel.contains(e.target)) toggle(false); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') toggle(false); });

  // 넓은 화면: 목차 띠 바로 아래에 붙여 둔다 (맨 위에서는 목차 띠를 따라 내려와 있다)
  const toc = document.querySelector('nav.toc');
  let ticking = false;
  function place() {
    ticking = false;
    if (narrow.matches) { panel.style.top = ''; return; }
    const top = toc ? toc.getBoundingClientRect().bottom : 0;
    panel.style.top = Math.max(top, 0) + 16 + 'px';
  }
  const req = () => { if (!ticking) { ticking = true; requestAnimationFrame(place); } };
  addEventListener('scroll', req, { passive: true });
  addEventListener('resize', req);
  narrow.addEventListener('change', () => { toggle(false); place(); });

  document.addEventListener('change', e => { if (e.target.matches && e.target.matches('input[data-check]')) update(); });
  update(); place();
})();
</script>"""

TABS_HTML = (
    '<div class="tabs-wrap"><nav class="tabs" aria-label="Day25 문서 탭">'
    '<a data-site href="../"><span class="n">1</span>사전 준비</a>'
    '<a data-site href="../spec/"><span class="n">2</span>요구사항 명세서</a>'
    '<a data-site href="./" aria-current="page"><span class="n">3</span>Basic 완주 안내</a>'
    '<a class="lec" data-site href="../lecture/">오전 강의 자료 →</a>'
    '</nav></div>'
)


def main() -> None:
    s = SRC.read_text(encoding="utf-8")

    # 1. 원본 목차만 가리키도록 nav 규칙을 좁힌다 (사이트 위쪽 메뉴는 sticky top:0이라 그 아래에 붙인다)
    s = replace_once(s, "nav{position:sticky;top:0;z-index:10;background:#fff;",
                     "nav.toc{position:sticky;top:48px;z-index:10;background:#fff;")
    s = replace_once(s, "nav a{font-size:13px;", "nav.toc a{font-size:13px;")
    s = replace_once(s, "nav a:hover{", "nav.toc a:hover{")
    s = replace_once(s, "nav{position:static;justify-content:flex-start}", "nav.toc{position:static;justify-content:flex-start}")
    s = replace_once(s, "nav{display:none}", "nav.toc{display:none}")
    s = replace_once(s, "nav{justify-content:flex-start}", "nav.toc{justify-content:flex-start}")
    s = replace_once(s, '<nav aria-label="목차">', '<nav class="toc" aria-label="목차">')

    # 2. 탭 줄
    s = replace_once(s, "</header>", "</header>" + TABS_HTML)

    # 3. 덧붙이는 CSS
    s = replace_once(s, "</style></head>", TABS_CSS + HEADER_CSS + FOLD_CSS + DARK_CSS + SPY_CSS + PROGRESS_CSS + "</style></head>")
    # 머리말 부제 두 줄을 한 줄로 (사용자 승인 2026-11-20: 탭을 바꿀 때 배너 높이가 1·2번 탭과 같게)
    s = replace_once(s, "검증까지<br>민준튜터개인용", "검증까지 · 민준튜터개인용")
    s = replace_once(s, "</body>", SPY_JS + PROGRESS_JS + "</body>")

    # 4. 개인 ChatGPT 라이브러리 링크 → 글자만
    s, n = re.subn(r'<a href="https://chatgpt\.com/[^"]*">(.*?)</a>', r"\1", s, flags=re.S)
    if n != 3:
        raise SystemExit(f"ChatGPT 링크가 {n}개 (3개여야 함). 원본을 확인하세요.")

    OUT.write_text(s, encoding="utf-8")
    print(f"{OUT.relative_to(HERE.parents[3])} ← {SRC.name}")


if __name__ == "__main__":
    main()
