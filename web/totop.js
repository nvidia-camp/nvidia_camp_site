/* =====================================================================
 * 맨 위로 버튼(.to-top) — 강의 요약·치트시트·설치 가이드 페이지
 *
 * - 한 화면의 60%쯤 내려가면 나타나고, 위로 돌아오면 사라진다.
 * - 테두리 원(.tt-bar)이 페이지를 읽은 만큼 찬다.
 * - 누르면 맨 위로 부드럽게 올라간다 (동작 줄이기 설정이면 바로 이동).
 * ===================================================================== */
(function () {
  var btn = document.querySelector('.to-top');
  if (!btn) return;
  var bar = btn.querySelector('.tt-bar');
  var LENGTH = 2 * Math.PI * 21;          // 원 둘레 (반지름 21)
  bar.style.strokeDasharray = LENGTH;
  var waiting = false;

  function update() {
    waiting = false;
    var root = document.documentElement;
    var y = window.scrollY || root.scrollTop;
    var max = root.scrollHeight - window.innerHeight;
    var read = max > 0 ? Math.min(1, y / max) : 0;
    bar.style.strokeDashoffset = LENGTH * (1 - read);
    btn.classList.toggle('show', y > window.innerHeight * 0.6);
  }

  function schedule() {
    if (!waiting) { waiting = true; requestAnimationFrame(update); }
  }

  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', schedule);
  window.addEventListener('load', update);
  update();

  btn.addEventListener('click', function () {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
  });
})();
