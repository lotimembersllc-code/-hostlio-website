// GA4 başlatması (yalnız build.py GA4_ID doluyken yüklenir). Satır içi betik yerine dosya: CSP script-src 'self' (O4).
(function () {
  var s = document.currentScript, id = s && s.getAttribute('data-ga');
  if (!id) return;
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', id);
})();
