// Appearance is the only client-side state; every page is readable without JS.
(() => {
  const button = document.querySelector('.theme-toggle');
  if (!button) return;
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  let preference;
  try { preference = localStorage.getItem('furong-theme'); } catch (_) { /* Storage may be unavailable. */ }
  function render() {
    const dark = preference ? preference === 'dark' : system.matches;
    document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
    button.textContent = dark ? 'Use light appearance' : 'Use dark appearance';
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
