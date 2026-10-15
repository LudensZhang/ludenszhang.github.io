/* Progressive enhancement: every section, link and the publication archive work without JavaScript. */
(() => {
  const portrait = document.querySelector('.portrait');
  if (portrait) {
    const hideBrokenPortrait = () => { portrait.hidden = true; };
    portrait.addEventListener('error', hideBrokenPortrait, { once: true });
    if (portrait.complete && !portrait.naturalWidth) hideBrokenPortrait();
  }

  // Header hairline and gold reading-progress bar.
  const header = document.querySelector('.site-header');
  let ticking = false;
  const onScroll = () => {
    ticking = false;
    const max = document.documentElement.scrollHeight - innerHeight;
    header.classList.toggle('scrolled', scrollY > 8);
    header.style.setProperty('--p', max > 0 ? Math.min(scrollY / max, 1).toFixed(4) : 0);
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
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

  // Active section in the navigation.
  const links = Array.from(document.querySelectorAll('nav a[href^="#"]'));
  const sections = links.map(link => document.querySelector(link.hash)).filter(Boolean);
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      for (const link of links) {
        if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      }
    }
  }, { rootMargin: '-20% 0px -55% 0px', threshold: 0 });
  sections.forEach(section => observer.observe(section));
  const hero = document.querySelector('#top');
  if (hero) new IntersectionObserver(entries => {
    if (entries.some(entry => entry.isIntersecting)) links.forEach(link => link.removeAttribute('aria-current'));
  }, { threshold: 0.4 }).observe(hero);
})();
