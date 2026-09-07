/* Progressive enhancement: navigation works with or without JavaScript. */
(() => {
  const portrait = document.querySelector('.portrait');
  if (portrait) {
    const hideBrokenPortrait = () => { portrait.hidden = true; };
    portrait.addEventListener('error', hideBrokenPortrait, { once: true });
    if (portrait.complete && !portrait.naturalWidth) hideBrokenPortrait();
  }
  const links = Array.from(document.querySelectorAll('nav a[href^="#"]'));
  if (!('IntersectionObserver' in window)) return;
  const sections = links.map(link => document.querySelector(link.hash)).filter(Boolean);
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      for (const link of links) {
        if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      }
    }
  }, { rootMargin: '-15% 0px -55% 0px', threshold: 0 });
  sections.forEach(section => observer.observe(section));
  const hero = document.querySelector('#top');
  if (hero) new IntersectionObserver(entries => {
    if (entries.some(entry => entry.isIntersecting)) links.forEach(link => link.removeAttribute('aria-current'));
  }, { threshold: 0.5 }).observe(hero);
})();
