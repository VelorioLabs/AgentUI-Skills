function setTheme(theme) {
  document.body.setAttribute('data-theme', theme);
  document.querySelectorAll('.theme-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
}

function toggleCmdPalette() {
  const modal = document.getElementById('cmdPalette');
  const isHidden = modal.style.display === 'none';
  modal.style.display = isHidden ? 'flex' : 'none';
  if (isHidden) document.getElementById('cmdInput').focus();
}

window.addEventListener('keydown', (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
    e.preventDefault();
    toggleCmdPalette();
  } else if (e.key === 'Escape') {
    document.getElementById('cmdPalette').style.display = 'none';
  }
});

function copyRecipe(name) {
  navigator.clipboard.writeText('<div class="bento-card">...</div>');
  alert("VibeUI Recipe copied to clipboard!");
}
