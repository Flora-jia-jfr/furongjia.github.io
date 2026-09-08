// Content and anchor navigation remain usable without JavaScript.
(() => {
  const button = document.querySelector('.theme-toggle');
  if (!button) return;
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  let preference;
  try { preference = localStorage.getItem('furong-theme'); } catch (_) { /* Storage may be unavailable. */ }
  function render() {
    const dark = preference ? preference === 'dark' : system.matches;
    document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    const label = dark ? 'Switch to light mode' : 'Switch to dark mode';
    button.setAttribute('aria-label', label);
    button.setAttribute('title', label);
  }
  button.hidden = false;
  button.addEventListener('click', () => {
    preference = document.documentElement.style.colorScheme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('furong-theme', preference); } catch (_) { /* Keep this page usable. */ }
    render();
  });
  system.addEventListener('change', render);
  render();
})();

// Highlight the homepage section currently in view, including direct deep links.
(() => {
  const sections = Array.from(document.querySelectorAll('.site-nav a[href^="#"]'))
    .map(link => ({ link, section: document.querySelector(link.getAttribute('href')) }))
    .filter(item => item.section);
  if (!sections.length) return;
  const header = document.querySelector('.site-header');
  let pending = false;
  function update() {
    pending = false;
    const threshold = header.getBoundingClientRect().bottom + 32;
    let active = sections[0];
    for (const item of sections) {
      if (item.section.getBoundingClientRect().top <= threshold) active = item;
    }
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) {
      active = sections[sections.length - 1];
    }
    for (const item of sections) {
      if (item === active) item.link.setAttribute('aria-current', 'location');
      else item.link.removeAttribute('aria-current');
    }
  }
  function schedule() {
    if (pending) return;
    pending = true;
    window.requestAnimationFrame(update);
  }
  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', schedule);
  window.addEventListener('hashchange', schedule);
  window.addEventListener('load', schedule);
  schedule();
})();
