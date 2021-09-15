function convert_webp(element) {
  let attribute = '';  // determine what attribute to query/change
  if (element.hasAttribute('src')) {
    attribute = 'src';
  } else if (element.hasAttribute('href')) {
    attribute = 'href';
  } else {
    console.warn('Unknown source attribute of ' + element);
    return;  // something else we don't know
  }

  let attrVal = element.getAttribute(attribute);
  let lastIndex = attrVal.lastIndexOf('.');
  let noSuffix = attrVal.slice(0, lastIndex);
  let fallback = element.getAttribute('data-fallback-filetype');
  if (fallback.startsWith('.')) {  // remove . if included
    fallback = fallback.slice(1);
  }

  let supportsWebp;  // whether or not we need to use the fallback
  switch (fallback) {
    case 'gif':
      supportsWebp = Modernizr.webp && Modernizr.webp.animation;
      break;
    case 'png':
      supportsWebp = Modernizr.webp && Modernizr.webp.alpha;
      break;
    default:
      supportsWebp = Modernizr.webp;
  }

  if (!supportsWebp) {
    element.setAttribute(attribute, noSuffix + '.' + fallback);
  }
}

// wait until we've tried to load all resources
window.onload = () => {
  // Query for all elements with a fallback filetype
  let elements = document.querySelectorAll('*[data-fallback-filetype]');
  for (let element of elements) {
    convert_webp(element);
  }
}
