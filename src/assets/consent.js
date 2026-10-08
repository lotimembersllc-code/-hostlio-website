// GA4 + Consent Mode v2 + çerez izni bandı (8 Ekim 2026, sahip kararı).
//
// Yalnız build.py'de GA4_ID doluyken sayfaya girer (<head>'de, async/defer DEĞİL: varsayılan izin
// durumu gtag.js'ten ÖNCE kuyruğa girmeli). Satır içi betik yok (CSP script-src 'self').
//
// Akış:
//  1. dataLayer + gtag kuyruğu kurulur; gtag('consent','default') ile DÖRT sinyal de 'denied'.
//     ad_storage / ad_user_data / ad_personalization HER ZAMAN denied kalır (reklam çalıştırmıyoruz).
//  2. Kayıtlı seçim yoksa bant gösterilir; gtag.js YÜKLENMEZ, Google'a tek istek gitmez ("basic"
//     consent mode: izinden önce çerezsiz ping de yok).
//  3. "Kabul et" → consent update analytics_storage=granted → gtag.js yüklenir → config (page_view).
//     "Reddet" → hiçbir şey yüklenmez; daha önce kabul edilmişse GA devre dışı bırakılır ve _ga
//     çerezleri silinir.
//  4. Seçim localStorage 'hostlio_consent' anahtarında 6 ay saklanır, sonra yeniden sorulur.
//     Altbilgideki "Çerez tercihleri" düğmesi ([data-consent-open]) bandı yeniden açar.
//
// Olaylar: diğer betikler window.hostlioTrack(ad, parametreler[, geri çağrı]) çağırır; izin yoksa
// hiçbir şey gönderilmez (kuyruğa da girmez). Olay adları ve parametreleri README "Analitik" bölümünde.
// Parametrelere ASLA e-posta, ad, telefon, otel adı gibi kişisel veri konmaz.
(function () {
  'use strict';
  var d = document, w = window, root = d.documentElement;
  var me = d.currentScript, ID = me && me.getAttribute('data-ga');
  if (!ID || !/^G-[A-Z0-9]+$/.test(ID)) return;
  var PRIVACY = {};
  try { PRIVACY = JSON.parse(me.getAttribute('data-privacy') || '{}'); } catch (e) {}

  var KEY = 'hostlio_consent', MAX_AGE = 182 * 24 * 3600 * 1000;   // ~6 ay
  var LANGS = ['tr', 'en', 'es', 'it', 'pt', 'fr'];
  var T = {
    tr: { h: 'Çerez tercihleri', p: 'Sitemizin nasıl kullanıldığını anlamak için, yalnızca izin verirseniz Google Analytics çerezleri kullanırız. Reklam çerezi kullanmayız. Seçiminizi istediğiniz zaman sayfanın altındaki “Çerez tercihleri” bağlantısından değiştirebilirsiniz.', more: 'Gizlilik Politikası', yes: 'Kabul et', no: 'Reddet', open: 'Çerez tercihleri' },
    en: { h: 'Cookie preferences', p: 'With your permission, we use Google Analytics cookies to understand how our website is used. We do not use advertising cookies. You can change your choice at any time via “Cookie preferences” at the bottom of the page.', more: 'Privacy Policy', yes: 'Accept', no: 'Reject', open: 'Cookie preferences' },
    es: { h: 'Preferencias de cookies', p: 'Solo con tu permiso usamos cookies de Google Analytics para entender cómo se usa nuestro sitio. No usamos cookies publicitarias. Puedes cambiar tu elección cuando quieras en “Preferencias de cookies”, al pie de la página.', more: 'Política de privacidad', yes: 'Aceptar', no: 'Rechazar', open: 'Preferencias de cookies' },
    it: { h: 'Preferenze cookie', p: 'Solo con il tuo consenso usiamo i cookie di Google Analytics per capire come viene usato il sito. Non usiamo cookie pubblicitari. Puoi cambiare la tua scelta in qualsiasi momento da “Preferenze cookie”, in fondo alla pagina.', more: 'Informativa sulla privacy', yes: 'Accetta', no: 'Rifiuta', open: 'Preferenze cookie' },
    pt: { h: 'Preferências de cookies', p: 'Só com a sua permissão usamos cookies do Google Analytics para entender como o site é usado. Não usamos cookies de publicidade. Você pode mudar sua escolha a qualquer momento em “Preferências de cookies”, no rodapé da página.', more: 'Política de privacidade', yes: 'Aceitar', no: 'Recusar', open: 'Preferências de cookies' },
    fr: { h: 'Préférences cookies', p: 'Uniquement avec votre accord, nous utilisons les cookies Google Analytics pour comprendre comment notre site est utilisé. Nous n’utilisons pas de cookies publicitaires. Vous pouvez modifier votre choix à tout moment via « Préférences cookies » en bas de page.', more: 'Politique de confidentialité', yes: 'Accepter', no: 'Refuser', open: 'Préférences cookies' }
  };

  // 1) Consent Mode v2 varsayılanları — gtag.js'ten önce
  w.dataLayer = w.dataLayer || [];
  function gtag() { w.dataLayer.push(arguments); }
  w.gtag = gtag;
  gtag('consent', 'default', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' });
  gtag('set', 'ads_data_redaction', true);

  function read() {
    try {
      var v = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (v && (v.s === 'granted' || v.s === 'denied') && typeof v.t === 'number' && Date.now() - v.t < MAX_AGE) return v.s;
    } catch (e) {}
    return null;
  }
  var mem = null;   // localStorage kapalıysa (özel pencere) seçim bu sayfa görüntülemesi boyunca bellekte
  function save(s) { mem = s; try { localStorage.setItem(KEY, JSON.stringify({ v: 1, s: s, t: Date.now() })); } catch (e) {} }
  var state = read();

  var loaded = false, configured = false;
  function load() {
    w['ga-disable-' + ID] = false;
    if (!configured) {
      configured = true;
      gtag('js', new Date());
      gtag('config', ID, { allow_google_signals: false, allow_ad_personalization_signals: false });
    }
    if (loaded) return;
    loaded = true;
    var s = d.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(ID);
    (d.head || root).appendChild(s);
  }
  function wipeCookies() {
    var host = location.hostname, parts = host.split('.'), doms = [''];
    for (var i = 0; i < parts.length - 1; i++) doms.push('.' + parts.slice(i).join('.'));
    d.cookie.split(';').forEach(function (c) {
      var n = c.split('=')[0].trim();
      if (n === '_ga' || n.indexOf('_ga_') === 0 || n === '_gid' || n === '_gat') {
        doms.forEach(function (dm) { d.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + (dm ? '; domain=' + dm : ''); });
      }
    });
  }
  function apply(s) {
    state = s;
    if (s === 'granted') {
      gtag('consent', 'update', { analytics_storage: 'granted' });
      load();
    } else {
      gtag('consent', 'update', { analytics_storage: 'denied' });
      w['ga-disable-' + ID] = true;
      wipeCookies();
    }
  }
  if (state === 'granted') apply('granted');

  // Olay yardımcısı: izin yoksa sessizce hiçbir şey yapmaz. cb verilirse gönderim kuyruğa alınınca
  // (en geç 900 ms) çağrılır.
  function granted() { return (state || mem) === 'granted'; }
  function copy(params) { var p = {}; for (var k in params || {}) if (Object.prototype.hasOwnProperty.call(params, k)) p[k] = params[k]; return p; }
  w.hostlioTrack = function (name, params, cb) {
    var done = false, fin = function () { if (!done) { done = true; if (cb) cb(); } };
    if (!granted()) { fin(); return; }
    var p = copy(params);
    if (cb) { p.event_callback = fin; p.event_timeout = 800; setTimeout(fin, 900); }
    gtag('event', name, p);
  };
  // Sayfadan ayrılmadan hemen önceki olaylar (kayıt CTA tıklaması, Stripe'a yönlendirme): gtag.js
  // olayları ~5 sn toplu gönderir ve hemen ayrılınca kaybolabiliyor (8 Eki testinde ölçüldü). Bu
  // olaylar sekmenin sessionStorage'ına yazılır, aynı sitedeki SONRAKİ sayfa açılışında (izin varsa)
  // gönderilir: CTA → kayıt sayfası, Stripe → /xx/signup/?checkout=… dönüşü. Çift sayım olmaz.
  var QKEY = 'hostlio_ga_q';
  w.hostlioTrack.defer = function (name, params) {
    if (!granted()) return;
    try {
      var q = JSON.parse(sessionStorage.getItem(QKEY) || '[]');
      q.push({ n: name, p: copy(params), t: Date.now() });
      sessionStorage.setItem(QKEY, JSON.stringify(q.slice(-10)));
    } catch (e) {}
  };
  function flush() {
    var q = [];
    try { q = JSON.parse(sessionStorage.getItem(QKEY) || '[]'); sessionStorage.removeItem(QKEY); } catch (e) {}
    if (!granted()) return;
    q.forEach(function (x) { if (x && x.n && Date.now() - x.t < 3600 * 1000) gtag('event', x.n, x.p || {}); });
  }
  flush();

  // ── bant
  function lang() {
    var m = location.pathname.match(/^\/(tr|en|es|it|pt|fr)(\/|$)/);
    if (m) return m[1];
    var l = (root.lang || '').slice(0, 2).toLowerCase();
    return LANGS.indexOf(l) > -1 ? l : 'en';
  }
  var box = null, opener = null;
  function el(tag, attrs, text) {
    var e = d.createElement(tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text) e.textContent = text;
    return e;
  }
  function texts() {
    var l = lang(), t = T[l] || T.en;
    if (box) {
      box.setAttribute('lang', l === 'pt' ? 'pt-BR' : l);
      box.querySelector('#consent-h').textContent = t.h;
      box.querySelector('.consent-text').textContent = t.p + ' ';
      var a = box.querySelector('.consent-more');
      a.textContent = t.more; a.href = (PRIVACY[l] || PRIVACY.en || '/en/privacy/') + '#cookies';
      box.querySelector('[data-consent="granted"]').textContent = t.yes;
      box.querySelector('[data-consent="denied"]').textContent = t.no;
    }
    [].forEach.call(d.querySelectorAll('[data-consent-open]'), function (b) { b.textContent = t.open; });
  }
  function build() {
    box = el('div', { 'class': 'consent', role: 'dialog', 'aria-modal': 'false', 'aria-labelledby': 'consent-h', 'aria-describedby': 'consent-d', tabindex: '-1', hidden: '' });
    var inner = el('div', { 'class': 'consent-in' });
    inner.appendChild(el('h2', { id: 'consent-h', 'class': 'consent-h' }));
    var p = el('p', { id: 'consent-d', 'class': 'consent-p' });
    p.appendChild(el('span', { 'class': 'consent-text' }));
    p.appendChild(el('a', { 'class': 'consent-more' }));
    inner.appendChild(p);
    var row = el('div', { 'class': 'consent-btns' });
    row.appendChild(el('button', { type: 'button', 'class': 'btn consent-btn', 'data-consent': 'denied' }));
    row.appendChild(el('button', { type: 'button', 'class': 'btn consent-btn', 'data-consent': 'granted' }));
    inner.appendChild(row);
    box.appendChild(inner);
    // DOM sırasında atlama bağlantısından hemen sonra: klavye kullanıcısı bandı ilk Tab'larda bulur
    var skip = d.querySelector('body > .skip');
    if (skip && skip.nextSibling) d.body.insertBefore(box, skip.nextSibling); else d.body.insertBefore(box, d.body.firstChild);
    row.addEventListener('click', function (e) {
      var b = e.target.closest('[data-consent]');
      if (!b) return;
      var s = b.getAttribute('data-consent');
      save(s); apply(s); hide(true);
      if (s === 'denied') try { sessionStorage.removeItem(QKEY); } catch (x) {}
    });
    box.addEventListener('keydown', function (e) {
      // Escape yalnız daha önce seçim yapılmışsa kapatır (seçim yapılmadan bant kaybolmaz)
      if (e.key === 'Escape' && (state || mem)) { e.stopPropagation(); hide(true); }
    });
    texts();
  }
  function show(focus) {
    if (!box) build();
    box.hidden = false;
    root.classList.add('consent-open');
    if (focus) box.focus();
  }
  function hide(returnFocus) {
    if (!box) return;
    var had = box.contains(d.activeElement);
    box.hidden = true;
    root.classList.remove('consent-open');
    if (had && returnFocus) {
      if (opener && d.body.contains(opener)) opener.focus();
      else { var m = d.getElementById('main'); if (m) { if (!m.hasAttribute('tabindex')) m.setAttribute('tabindex', '-1'); m.focus({ preventScroll: true }); } }
    }
    opener = null;
  }

  function init() {
    [].forEach.call(d.querySelectorAll('[data-consent-open]'), function (b) {
      b.hidden = false;
      b.addEventListener('click', function () { opener = b; show(true); });
    });
    texts();
    if (!state) show(false);
    // dil sonradan değişirse (kök /signup/ dil algılaması, 404 sayfası) metinler yeniden yazılır
    if (w.MutationObserver) new MutationObserver(texts).observe(root, { attributes: true, attributeFilter: ['lang'] });

    // Kayıt CTA tıklamaları (tüm sayfalar): /xx/signup/ bağlantıları
    d.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href]');
      if (!a) return;
      var u;
      try { u = new URL(a.getAttribute('href'), location.href); } catch (x) { return; }
      if (u.origin !== location.origin || !/^\/((tr|en|es|it|pt|fr)\/)?signup\/$/.test(u.pathname)) return;
      var where = a.closest('header') ? 'header' : a.closest('footer') ? 'footer' : a.closest('.plans,.plan,.annual-table') ? 'pricing_plans'
        : a.closest('.final') ? 'final_cta' : a.closest('.hero,.page-hero') ? 'hero' : 'content';
      var prm = { cta_location: where, cta_page: location.pathname };
      if (u.searchParams.get('plan')) prm.plan = u.searchParams.get('plan');
      if (u.searchParams.get('billing')) prm.billing = u.searchParams.get('billing');
      w.hostlioTrack.defer('signup_cta_click', prm);   // kayıt sayfası açılınca gönderilir
    }, true);
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', init); else init();
})();
