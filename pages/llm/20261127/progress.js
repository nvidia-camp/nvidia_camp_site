(() => {
  const inputs = [...document.querySelectorAll('input[data-check]')];
  if (!inputs.length) return;
  const tocText = id => (document.querySelector('nav.toc a[href="#' + id + '"]') || {}).textContent || '';
  const groups = [
    { key: 'step', label: '구현·검증 단계', items: [] },
    { key: 'postman', label: 'Postman 요청', items: [] },
    { key: 'finish', label: '완료 기준', items: [] },
  ];
  inputs.forEach(input => {
    const sec = input.closest('section');
    const id = sec ? sec.id : '';
    const g = id === 'postman' ? groups[1] : id === 'finish' ? groups[2] : groups[0];
    const text = (input.closest('.checkline') || input.parentElement).textContent.trim();
    const name = g.key === 'postman'
      ? input.closest('.request-card')?.querySelector('h3, h4')?.textContent.trim() || text
      : [tocText(id), text].filter(Boolean).join(' · ');
    g.items.push({ input, name });
  });
  const all = groups.flatMap(g => g.items);

  const panel = document.createElement('aside');
  panel.className = 'pg';
  panel.id = 'basic-progress';
  panel.setAttribute('aria-label', '체크 진행 상황');
  panel.innerHTML = '<div class="pg-head"><b>진행 상황</b><span class="pg-num"></span></div><div class="pg-bar"><span></span></div>' +
    groups.map(g => '<div class="pg-g"><div class="pg-g-h">' + g.label + '<span></span></div><div class="pg-cells"></div></div>').join('') +
    '<button type="button" class="pg-next"></button><div class="pg-clear"></div>';
  const chip = document.createElement('button');
  chip.type = 'button';
  chip.className = 'pg-chip';
  chip.setAttribute('aria-expanded', 'false');
  chip.setAttribute('aria-controls', panel.id);
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
  const motion = matchMedia('(prefers-reduced-motion: reduce)');

  function go(item) {
    const line = item.input.closest('.checkline') || item.input;
    line.scrollIntoView({ behavior: motion.matches ? 'auto' : 'smooth', block: 'center' });
    line.classList.remove('pg-flash'); void line.offsetWidth; line.classList.add('pg-flash');
    if (narrow.matches) toggle(false);
    item.input.focus({ preventScroll: true });
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
      clear.querySelector('.pg-no').onclick = () => {
        confirming = false;
        update();
        clear.querySelector('button').focus();
      };
    } else {
      confirming = false;
      clear.innerHTML = '<button type="button">전체 지우기</button>';
      const b = clear.querySelector('button');
      b.disabled = !done;
      b.onclick = () => {
        confirming = true;
        update();
        clear.querySelector('.pg-no')?.focus();
      };
    }
  }

  function toggle(open) {
    panel.classList.toggle('open', open);
    chip.setAttribute('aria-expanded', String(open));
  }
  chip.addEventListener('click', e => { e.stopPropagation(); toggle(!panel.classList.contains('open')); });
  document.addEventListener('click', e => { if (narrow.matches && panel.classList.contains('open') && !panel.contains(e.target)) toggle(false); });

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
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && panel.classList.contains('open')) {
      toggle(false);
      chip.focus();
    }
  });
  narrow.addEventListener('change', () => { toggle(false); place(); });

  document.addEventListener('change', e => {
    if (!(e.target.matches && e.target.matches('input[data-check]'))) return;
    update();
    panel.classList.remove('bump'); void panel.offsetWidth; panel.classList.add('bump');   // 체크가 반영됐다는 것을 보여 준다
  });
  update(); place();
})();
