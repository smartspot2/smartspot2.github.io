// Handle preview and pausing of animated images
const freezeframes = document.getElementsByClassName('freezeframe');

for (let div of freezeframes) {
  let overlay = div.getElementsByClassName('freezeframe-overlay').item(0);
  let gif = div.getElementsByClassName('freezeframe-gif').item(0);
  let img = new Image();
  img.src = gif.src;  // preload image

  overlay.addEventListener('mouseenter', () => {
    overlay.style.opacity = '0';
    gif.setAttribute('src', img.src)  // reset src to reload gif
  });
  overlay.addEventListener('mouseleave', () => {
    overlay.style.opacity = '1';
  });
}

// Copy email to clipboard

let emailLink = document.getElementById('intro-email-link');
let emaillinkTooltip = new bootstrap.Tooltip(emailLink,
    {
      'trigger': 'manual',
      'placement': 'bottom',
      'title': 'Copied to clipboard!'
    }
);
emailLink.addEventListener('click', () => {
  // Yeah no you're not gonna get the email that easily from web scraping.
  let encoded = 'PTAyYmo1Q2JwRldibkJrTTA5R2N6Um5jaDEyYw==';  // personal
  // let encoded = 'PVVIWmw1U2VseFdackpYWmlCVWFzNXlZbHhXWQ==';  // berkeley
  let textArea = document.createElement('textarea');
  textArea.value = atob(atob(encoded).split('').reverse().join(''));
  textArea.style.opacity = '0';
  emailLink.appendChild(textArea);
  textArea.focus();
  textArea.select();
  document.execCommand('copy');
  emailLink.removeChild(textArea);
  emaillinkTooltip.show();
  setTimeout(() => {
    emaillinkTooltip.hide()
  }, 1000);
});
