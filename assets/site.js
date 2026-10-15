/* Progressive enhancement: every section, link and the publication archive work without JavaScript. */
(() => {
  const portrait = document.querySelector('.portrait');
  if (portrait) {
    const hideBrokenPortrait = () => { portrait.hidden = true; };
    portrait.addEventListener('error', hideBrokenPortrait, { once: true });
    if (portrait.complete && !portrait.naturalWidth) hideBrokenPortrait();
  }

  // Read the section at a stable reading line, including after viewport changes.
  const links = Array.from(document.querySelectorAll('nav a[href^="#"]'));
  const sections = links.map(link => document.querySelector(link.hash)).filter(Boolean);

  // Header hairline and gold reading-progress bar.
  const header = document.querySelector('.site-header');
  let ticking = false;
  const onScroll = () => {
    ticking = false;
    const max = document.documentElement.scrollHeight - innerHeight;
    header.classList.toggle('scrolled', scrollY > 8);
    header.style.setProperty('--p', max > 0 ? Math.min(scrollY / max, 1).toFixed(4) : 0);
    const readingLine = Math.max(header.getBoundingClientRect().height + 24, innerHeight * 0.25);
    const active = sections.filter(section => section.getBoundingClientRect().top <= readingLine).pop();
    for (const link of links) {
      if (active && link.hash === `#${active.id}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    }
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  onScroll();

  // Publication filters inside the archive.
  const filters = document.querySelector('.filters');
  if (filters) {
    const archive = filters.closest('.archive');
    const papers = Array.from(archive.querySelectorAll('.paper'));
    const years = Array.from(archive.querySelectorAll('.archive-year'));
    const count = filters.querySelector('.filter-count');
    const apply = filter => {
      let shown = 0;
      for (const paper of papers) {
        const match = filter === 'all' || (filter === 'first' ? paper.dataset.first === 'true' : paper.dataset.kind === filter);
        paper.hidden = !match;
        if (match) shown += 1;
      }
      for (const year of years) year.hidden = !year.querySelector('.paper:not([hidden])');
      count.textContent = `${shown} of ${papers.length} shown`;
      for (const button of filters.querySelectorAll('button')) button.setAttribute('aria-pressed', String(button.dataset.filter === filter));
    };
    filters.addEventListener('click', event => {
      const button = event.target.closest('button[data-filter]');
      if (button) apply(button.dataset.filter);
    });
    filters.hidden = false;
    apply('all');
  }

  if (!('IntersectionObserver' in window)) return;

  // Pause decorative loops outside the viewport; real content stays independent.
  const motionObserver = new IntersectionObserver(entries => {
    for (const entry of entries) entry.target.classList.toggle('motion-paused', !entry.isIntersecting);
  }, { rootMargin: '120px' });
  document.querySelectorAll('.motion-art').forEach(element => motionObserver.observe(element));


  // Gentle reveal for content that starts below the fold; visible content is never hidden.
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.documentElement.classList.add('js');
    const revealables = document.querySelectorAll('.section-head, .about-body, .education, .cv, .direction, .feature-text, .feature-figure, .stats > div, .selected > .paper, .archive, .project, .footer-main');
    const revealer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('is-visible');
        revealer.unobserve(entry.target);
      }
    }, { rootMargin: '0px 0px -6% 0px' });
    revealables.forEach((element, index) => {
      if (element.getBoundingClientRect().top < innerHeight) return;
      element.classList.add('reveal');
      element.style.transitionDelay = `${(index % 3) * 80}ms`;
      revealer.observe(element);
    });
  }

})();
