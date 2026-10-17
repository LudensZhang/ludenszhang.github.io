(() => {
  'use strict';

  const progress = document.getElementById('read-progress');
  const onScroll = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)) : 0;
    if (progress) progress.style.transform = `scaleX(${ratio})`;
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);

  const navLinks = [...document.querySelectorAll('[data-nav-link]')];
  const sections = [...document.querySelectorAll('[data-nav]')];
  const setCurrent = (id) => {
    for (const link of navLinks) {
      const on = link.dataset.navLink === id;
      if (on) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    }
  };
  if ('IntersectionObserver' in window && sections.length) {
    const spy = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible) setCurrent(visible.target.dataset.nav);
    }, { rootMargin: '-30% 0px -55% 0px', threshold: [0, 0.2, 0.6] });
    sections.forEach((section) => spy.observe(section));
  }

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-theme-jump]').forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      const theme = link.dataset.themeJump;
      const group = document.querySelector('[data-group="theme"]');
      if (group) press(group, theme);
      const query = document.getElementById('q');
      if (query) query.value = '';
      press(document.querySelector('[data-group="year"]'), '');
      press(document.querySelector('[data-group="kind"]'), '');
      apply();
      const target = document.getElementById('publications-title');
      if (target) {
        target.scrollIntoView({ behavior: reduce.matches ? 'auto' : 'smooth', block: 'start' });
        target.focus({ preventScroll: true });
      }
      const url = new URL(location.href);
      url.searchParams.set('theme', theme);
      url.searchParams.delete('q');
      url.searchParams.delete('year');
      url.searchParams.delete('kind');
      url.hash = 'publications';
      history.replaceState(null, '', url);
    });
  });

  const form = document.querySelector('.tools');
  if (!form) return;
  const records = [...document.querySelectorAll('.paper')];
  const total = records.length;
  const query = document.getElementById('q');
  const count = document.querySelector('.count');
  const empty = document.querySelector('.empty');
  const clear = form.querySelector('.clear');
  const live = document.querySelector('.announcement');
  const state = { year: '', kind: '', theme: '' };

  function press(group, value) {
    if (!group) return;
    const buttons = [...group.querySelectorAll('button')];
    const known = buttons.some((button) => button.dataset.value === value);
    const next = known ? value : '';
    state[group.dataset.group] = next;
    for (const button of buttons) {
      button.setAttribute('aria-pressed', button.dataset.value === next ? 'true' : 'false');
    }
  }

  function apply() {
    const words = query.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const record of records) {
      const themes = (record.dataset.themes || '').split(/\s+/).filter(Boolean);
      const ok = (!state.year || record.dataset.year === state.year)
        && (!state.kind || record.dataset.kind === state.kind)
        && (!state.theme || themes.includes(state.theme))
        && words.every((word) => record.dataset.search.includes(word));
      record.hidden = !ok;
      if (ok) shown += 1;
    }
    count.textContent = shown === total ? `${total} papers` : `${shown} of ${total}`;
    empty.hidden = shown > 0;
    const active = Boolean(state.year || state.kind || state.theme || query.value.trim());
    clear.hidden = !active;
  }

  form.addEventListener('submit', (event) => { event.preventDefault(); apply(); });
  query.addEventListener('input', apply);
  query.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      query.value = '';
      apply();
    }
  });
  form.querySelectorAll('.toggles').forEach((group) => {
    group.addEventListener('click', (event) => {
      const button = event.target.closest('button');
      if (!button || !group.contains(button)) return;
      press(group, button.dataset.value);
      apply();
    });
  });
  clear.addEventListener('click', () => {
    query.value = '';
    form.querySelectorAll('.toggles').forEach((group) => press(group, ''));
    apply();
    query.focus();
  });

  const params = new URLSearchParams(location.search);
  if (params.get('q')) query.value = params.get('q');
  press(document.querySelector('[data-group="year"]'), params.get('year') || '');
  press(document.querySelector('[data-group="kind"]'), params.get('kind') || '');
  press(document.querySelector('[data-group="theme"]'), params.get('theme') || '');
  apply();

  document.querySelectorAll('.copy-citation').forEach((button) => {
    button.addEventListener('click', async () => {
      const citation = button.dataset.citation || '';
      try {
        await navigator.clipboard.writeText(citation);
        button.textContent = 'Copied';
        button.classList.add('is-copied');
        if (live) live.textContent = 'Citation copied to clipboard';
        window.setTimeout(() => {
          button.textContent = 'Copy citation';
          button.classList.remove('is-copied');
        }, 2000);
      } catch {
        let field = button.parentElement.querySelector('.cite-fallback');
        if (!field) {
          field = document.createElement('textarea');
          field.className = 'cite-fallback';
          field.readOnly = true;
          field.value = citation;
          field.setAttribute('aria-label', 'Citation');
          button.parentElement.append(field);
        }
        field.focus();
        field.select();
        button.textContent = 'Select the citation';
        if (live) live.textContent = 'Clipboard unavailable. The citation is selected in a text box.';
      }
    });
  });
})();
