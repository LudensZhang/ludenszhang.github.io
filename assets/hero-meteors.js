/* Occasional meteors only. Claude's original hero SVG/CSS animations are untouched. */
(() => {
  const scene = document.querySelector('.hero-meteors');
  if (!scene) return;
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const meteor = scene.querySelector('.hero-meteor');
  const meteorHead = meteor.querySelector('.meteor-head');
  const meteorTail = Array.from(meteor.querySelectorAll('.meteor-tail'));
  // Deliberately sparse and varied; at most one flat streak is visible at once.
  const meteorPaths = [[550, 130, 240, 280], [400, 90, 130, 260], [560, 350, 320, 470], [510, 180, 200, 340]];
  const meteorGaps = [13, 19, 16, 23];
  let nextMeteor = 6;
  let meteorIndex = 0;
  const renderMeteor = seconds => {
    const phase = (seconds - nextMeteor) / 1.4;
    if (phase < 0) { meteor.setAttribute('opacity', '0'); return; }
    if (phase >= 1) {
      meteor.setAttribute('opacity', '0');
      nextMeteor += 1.4 + meteorGaps[meteorIndex % meteorGaps.length];
      meteorIndex += 1;
      return;
    }
    const [x1, y1, x2, y2] = meteorPaths[meteorIndex % meteorPaths.length];
    const dx = x2 - x1;
    const dy = y2 - y1;
    const length = Math.hypot(dx, dy);
    const x = x1 + dx * phase;
    const y = y1 + dy * phase;
    meteor.setAttribute('opacity', Math.min(1, phase / .12, (1 - phase) / .3).toFixed(3));
    meteorHead.setAttribute('cx', x.toFixed(2));
    meteorHead.setAttribute('cy', y.toFixed(2));
    // Three flat stroke weights taper the tail, without gradients or blur.
    const offsets = [[76, 44], [44, 16], [16, 0]];
    meteorTail.forEach((tail, index) => {
      const [a, b] = offsets[index];
      tail.setAttribute('d', `M${(x - dx / length * a).toFixed(2)} ${(y - dy / length * a).toFixed(2)}L${(x - dx / length * b).toFixed(2)} ${(y - dy / length * b).toFixed(2)}`);
    });
  };
  let inView = true;
  let frame = 0;
  let last = null;
  let elapsed = 0;
  let lastPaint = -Infinity;
  const tick = now => {
    if (last !== null) elapsed += (now - last) / 1000;
    last = now;
    if (now - lastPaint >= 1000 / 30) { renderMeteor(elapsed); lastPaint = now; }
    frame = requestAnimationFrame(tick);
  };
  const sync = () => {
    cancelAnimationFrame(frame);
    frame = 0;
    last = null;
    const running = !motion.matches && inView && !document.hidden;
    if (motion.matches) {
      meteor.setAttribute('opacity', '0');
    } else if (running) frame = requestAnimationFrame(tick);
  };
  document.addEventListener('visibilitychange', sync);
  motion.addEventListener('change', sync);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(([entry]) => { inView = entry.isIntersecting; sync(); }).observe(scene.closest('.hero-art'));
  }
  sync();
})();
