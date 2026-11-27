(() => {
  const toc = document.querySelector('nav.toc');
  const root = document.documentElement;
  const siteBar = document.querySelector('.cn-nav');
  const links = [...toc.querySelectorAll('a[href^="#"]')];
  const sections = links.map(link => ({
    link,
    target: document.getElementById(link.hash.slice(1)),
  })).filter(item => item.target);
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  if (!siteBar) {
    const colorPreference = matchMedia('(prefers-color-scheme: dark)');
    const syncTheme = () => { root.dataset.theme = colorPreference.matches ? 'dark' : 'light'; };
    syncTheme();
    colorPreference.addEventListener('change', syncTheme);
  }
  let current;
  let pending = false;

  function measure() {
    const navHeight = siteBar?.getBoundingClientRect().height || 0;
    const offset = navHeight + toc.getBoundingClientRect().height;
    root.style.setProperty('--day30-nav-height', navHeight + 'px');
    root.style.setProperty('--day30-sticky', offset + 'px');
    root.style.scrollPaddingTop = (offset + 14) + 'px';
  }

  function markActive() {
    pending = false;
    const line = toc.getBoundingClientRect().bottom + 30;
    let active = sections[0];
    for (const item of sections) {
      if (item.target.getBoundingClientRect().top <= line) active = item;
    }
    if (scrollY + innerHeight >= root.scrollHeight - 3) active = sections.at(-1);
    if (!active || current === active.link) return;
    current?.removeAttribute('aria-current');
    current = active.link;
    current.setAttribute('aria-current', 'location');
    const { left, width } = current.getBoundingClientRect();
    const bounds = toc.getBoundingClientRect();
    toc.scrollTo({
      left: toc.scrollLeft + left - bounds.left - (bounds.width - width) / 2,
      behavior: reducedMotion.matches ? 'instant' : 'smooth',
    });
  }

  function schedule() {
    if (pending) return;
    pending = true;
    requestAnimationFrame(markActive);
  }

  const observer = new ResizeObserver(() => { measure(); schedule(); });
  observer.observe(toc);
  if (siteBar) observer.observe(siteBar);
  addEventListener('scroll', schedule, { passive: true });
  measure();
  markActive();
})();
