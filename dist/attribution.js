// A2 — PAZARLAMA KAYNAĞI YAKALAMA (İLK TEMAS)
//
// 🔺 NEDEN VAR: `signup_attempts` bugüne kadar ip / ip_source / email_hash /
// outcome tutuyordu; hangi müşterinin hangi reklamdan geldiği HİÇBİR YERDE
// yazmıyordu. Reklam bütçesi bu veri olmadan ölçülemez. Kalem GERİYE DÖNÜK
// ÜRETİLEMEZ: dün gelen ziyaretçinin kaynağı bugün öğrenilemez.
//
// ══ TASARIM KARARI 1: İLK TEMAS (FIRST-TOUCH), SON TEMAS DEĞİL ══
//
// İlk kayıt KAZANIR, üstüne yazılmaz. Gerçek yol şöyle: reklamdan bir blog
// yazısına düşer → birkaç gün sonra doğrudan girip kaydolur. Son temas modeli
// bu müşteriyi "direct" sayar ve reklamı BEDAVA gösterir. SEO için yazılmış
// blog yazılarının dönüşüm getirip getirmediğini ölçecek olan da tam budur.
//
// ══ TASARIM KARARI 2: HER SAYFAYA GİRER ══
//
// Yalnız index + signup'a konsaydı, reklamdan blog yazısına düşen ziyaretçinin
// kaynağı KAYBOLURDU — üstelik tam da ölçmek istediğimiz yol o. Betik bu
// yüzden 15 sayfanın hepsinde; yeni sayfa eklerken de eklenmeli.
//
// ══ TASARIM KARARI 3: ARIZASI SESSİZ VE ZARARSIZ ══
//
// localStorage özel pencerede / çerez engelliyken YAZARKEN DE OKURKEN DE
// istisna atabiliyor. Her erişim try/catch içinde ve bellek içi yedeği var:
// ölçüm kaybolur ama KAYIT FORMU ÇALIŞMAYA DEVAM EDER. Ölçüm uğruna satış
// kaybedilmez.

(function () {
  'use strict';

  var KEY = 'hostlio_acq';
  var MAX = 200;              // alan başına karakter tavanı (Stripe metadata 500)
  var memory = null;          // localStorage yazılamıyorsa bu sayfa ömrü kadar yedek

  function trim(v) {
    if (v === null || v === undefined) return null;
    var s = String(v).trim();
    if (!s) return null;
    return s.length > MAX ? s.slice(0, MAX) : s;
  }

  function read() {
    try {
      var raw = window.localStorage.getItem(KEY);
      if (raw) {
        var parsed = JSON.parse(raw);
        // Biçimi tanınmayan eski/bozuk kayıt ilk temas sayılmaz.
        if (parsed && typeof parsed === 'object' && parsed.first_seen) return parsed;
      }
    } catch (_e) { /* özel pencere / engelli depolama */ }
    return memory;
  }

  function write(rec) {
    memory = rec;
    try { window.localStorage.setItem(KEY, JSON.stringify(rec)); } catch (_e) { /* yedek bellekte */ }
  }

  // Reklam tıklama kimlikleri. Değer TAŞINIYOR; `medium` çıkarımı ayrı.
  // 🔺 `fbclid` BİLİNÇLİ OLARAK 'cpc' SAYILMIYOR: organik bir Facebook
  //    paylaşımına tıklayan ziyaretçide de bulunuyor. Ücretli demek, ücretsiz
  //    trafiği reklam hanesine yazmak olurdu.
  var CLICK_IDS = [
    { param: 'gclid',   source: 'google',    medium: 'cpc' },
    { param: 'msclkid', source: 'bing',      medium: 'cpc' },
    { param: 'ttclid',  source: 'tiktok',    medium: 'cpc' },
    { param: 'fbclid',  source: 'facebook',  medium: 'social' }
  ];

  function capture() {
    var params;
    try { params = new URLSearchParams(window.location.search); } catch (_e) { params = null; }
    var q = function (name) { return params ? trim(params.get(name)) : null; };

    var rec = {
      source:    q('utm_source'),
      medium:    q('utm_medium'),
      campaign:  q('utm_campaign'),
      term:      q('utm_term'),
      content:   q('utm_content'),
      click_id:  null,
      referrer:  null,
      landing:   trim(window.location.pathname) || '/',
      first_seen: new Date().toISOString()
    };

    // Tıklama kimliği: değeri sakla, kaynağı YALNIZ utm yoksa ondan türet.
    for (var i = 0; i < CLICK_IDS.length; i++) {
      var c = CLICK_IDS[i];
      var v = q(c.param);
      if (!v) continue;
      rec.click_id = c.param + ':' + v;
      if (!rec.source) rec.source = c.source;
      if (!rec.medium) rec.medium = c.medium;
      break;
    }

    // Dış yönlendiren. Kendi alan adımız yönlendiren SAYILMAZ (iç gezinme).
    // 🔺 Yalnız HOST saklanıyor, tam URL değil: yönlendiren adresin sorgu
    //    dizesi kişisel veri taşıyabilir ve bize hiçbir şey katmıyor.
    try {
      if (document.referrer) {
        var host = new URL(document.referrer).hostname;
        if (host && host !== window.location.hostname) {
          rec.referrer = trim(host);
          if (!rec.source) rec.source = trim(host);
          if (!rec.medium) rec.medium = 'referral';
        }
      }
    } catch (_e) { /* referrer ayrıştırılamadı — alan boş kalır */ }

    if (!rec.source) { rec.source = 'direct'; rec.medium = 'none'; }
    return rec;
  }

  // İlk temas yoksa yaz. VARSA DOKUNMA — modelin tamamı bu satırda.
  var current = read();
  if (!current) { current = capture(); write(current); }

  // Kayıt formunun okuduğu yüzey. signup.html bunu `fetch` gövdesine ekliyor.
  // Betik yüklenmediyse `undefined` döner ve form eskisi gibi çalışır.
  window.hostlioAcq = function () {
    var r = read();
    if (!r) return null;
    return {
      acq_source:     r.source || null,
      acq_medium:     r.medium || null,
      acq_campaign:   r.campaign || null,
      acq_term:       r.term || null,
      acq_content:    r.content || null,
      acq_click_id:   r.click_id || null,
      acq_referrer:   r.referrer || null,
      acq_landing:    r.landing || null,
      acq_first_seen: r.first_seen || null
    };
  };
})();
