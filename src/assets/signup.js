// Kayıt / ödeme sayfası (/xx/signup/ ve dil algılayan /signup/).
// Eski src_legacy/signup_script.js + assets/checkout.js birleşimi (L2, O4: satır içi betik yok).
// Ödeme oturumu SUNUCUDA açılır (signup-checkout); buradaki kontroller ilk savunma katmanı.
// Metinler: <script type="application/json" id="co-data"> (signup_page.py).
// Fiyatlar: /assets/prices.js (tek kaynak pricing.py + canlı `plans` ucu, early_bird bayrağı).
(function () {
'use strict';
var d = document;
var CO;
try { CO = JSON.parse(d.getElementById('co-data').textContent); } catch (e) { return; }
var L = ['en', 'tr', 'es', 'it', 'pt', 'fr'];
var SIGNUP_CHECKOUT_URL = 'https://brzetctpyaxognnvjrnd.supabase.co/functions/v1/signup-checkout';

// ── dil: sabit (/xx/signup/) ya da ?lang= → localStorage → yönlendiren sayfa → tarayıcı → en
(function () {
  if (CO.fixed) { CO.lang = CO.fixed; return; }
  var q = new URLSearchParams(location.search).get('lang'), l = null;
  if (L.indexOf(q) > -1) l = q;
  if (!l) { try { var v = localStorage.getItem('hostlio_lang'); if (L.indexOf(v) > -1) l = v; } catch (e) {} }
  if (!l && d.referrer) { try { var r = new URL(d.referrer); if (r.host === location.host) { var m = r.pathname.match(/^\/(en|tr|es|it|pt|fr)\//); if (m) l = m[1]; } } catch (e) {} }
  if (!l) { var n = (navigator.language || 'en').slice(0, 2).toLowerCase(); l = L.indexOf(n) > -1 ? n : 'en'; }
  CO.lang = l;
})();
function tr(k) { var S = CO.S; return (S[CO.lang] && S[CO.lang][k]) || S.en[k] || k; }

// ── fiyatlar (prices.js yoksa sayfaya gömülü statik değerler)
var HP = window.HostlioPrices;
function P() { return HP ? HP.config.plans : CO.PLANS; }
function eb() { return HP ? HP.config.early_bird : CO.EARLY_BIRD; }
function money(n) { return HP ? HP.money(n, CO.lang) : '$' + n; }
var isAnnual = false;
function priceOf(id) { var p = P()[id]; return isAnnual ? Math.round(p.a / 12) : p.m; }

// ── ÜLKE → PARA BİRİMİ + SAAT DİLİMİ ────────────────────────────────────────
// Dış kütüphane YOK — statik tablo. Alanlar: [ISO 3166-1 alpha-2, ad,
// ISO 4217, varsayılan IANA saat dilimi, (opsiyonel) o ülkedeki diğer zonlar].
//
// `zones` NEDEN VAR: tarayıcı tahmini o ülkenin zonlarından biriyse KORUNUR.
// ABD'li bir otelci America/Chicago'dayken ülkeyi US seçince tahmini
// America/New_York'a ezmek, düzeltmeyi otelciye bırakmak olurdu — ve §5'teki
// arıza tam olarak "otelci Ayarlar'ı hiç açmıyor" durumu.
const COUNTRIES = [
  ['AE','United Arab Emirates','AED','Asia/Dubai'],
  ['AL','Albania','ALL','Europe/Tirane'],
  ['AR','Argentina','ARS','America/Argentina/Buenos_Aires'],
  ['AT','Austria','EUR','Europe/Vienna'],
  ['AU','Australia','AUD','Australia/Sydney',['Australia/Sydney','Australia/Melbourne','Australia/Brisbane','Australia/Adelaide','Australia/Perth','Australia/Darwin','Australia/Hobart']],
  ['AZ','Azerbaijan','AZN','Asia/Baku'],
  ['BE','Belgium','EUR','Europe/Brussels'],
  ['BG','Bulgaria','EUR','Europe/Sofia'],
  ['BR','Brazil','BRL','America/Sao_Paulo',['America/Sao_Paulo','America/Bahia','America/Fortaleza','America/Manaus','America/Recife']],
  ['CA','Canada','CAD','America/Toronto',['America/Toronto','America/Vancouver','America/Edmonton','America/Winnipeg','America/Halifax','America/St_Johns']],
  ['CH','Switzerland','CHF','Europe/Zurich'],
  ['CL','Chile','CLP','America/Santiago'],
  ['CN','China','CNY','Asia/Shanghai'],
  ['CO','Colombia','COP','America/Bogota'],
  ['CY','Cyprus','EUR','Asia/Nicosia'],
  ['CZ','Czechia','CZK','Europe/Prague'],
  ['DE','Germany','EUR','Europe/Berlin'],
  ['DK','Denmark','DKK','Europe/Copenhagen'],
  ['EG','Egypt','EGP','Africa/Cairo'],
  ['ES','Spain','EUR','Europe/Madrid',['Europe/Madrid','Atlantic/Canary']],
  ['FI','Finland','EUR','Europe/Helsinki'],
  ['FR','France','EUR','Europe/Paris'],
  ['GB','United Kingdom','GBP','Europe/London'],
  ['GE','Georgia','GEL','Asia/Tbilisi'],
  ['GR','Greece','EUR','Europe/Athens'],
  ['HR','Croatia','EUR','Europe/Zagreb'],
  ['HU','Hungary','HUF','Europe/Budapest'],
  ['ID','Indonesia','IDR','Asia/Jakarta',['Asia/Jakarta','Asia/Makassar','Asia/Jayapura']],
  ['IE','Ireland','EUR','Europe/Dublin'],
  ['IL','Israel','ILS','Asia/Jerusalem'],
  ['IN','India','INR','Asia/Kolkata'],
  ['IT','Italy','EUR','Europe/Rome'],
  ['JP','Japan','JPY','Asia/Tokyo'],
  ['KE','Kenya','KES','Africa/Nairobi'],
  ['KR','South Korea','KRW','Asia/Seoul'],
  ['MA','Morocco','MAD','Africa/Casablanca'],
  ['ME','Montenegro','EUR','Europe/Podgorica'],
  ['MT','Malta','EUR','Europe/Malta'],
  ['MX','Mexico','MXN','America/Mexico_City',['America/Mexico_City','America/Cancun','America/Monterrey','America/Tijuana']],
  ['MY','Malaysia','MYR','Asia/Kuala_Lumpur'],
  ['NG','Nigeria','NGN','Africa/Lagos'],
  ['NL','Netherlands','EUR','Europe/Amsterdam'],
  ['NO','Norway','NOK','Europe/Oslo'],
  ['NZ','New Zealand','NZD','Pacific/Auckland'],
  ['PE','Peru','PEN','America/Lima'],
  ['PH','Philippines','PHP','Asia/Manila'],
  ['PL','Poland','PLN','Europe/Warsaw'],
  ['PT','Portugal','EUR','Europe/Lisbon',['Europe/Lisbon','Atlantic/Madeira','Atlantic/Azores']],
  ['QA','Qatar','QAR','Asia/Qatar'],
  ['RO','Romania','RON','Europe/Bucharest'],
  ['RS','Serbia','RSD','Europe/Belgrade'],
  ['SA','Saudi Arabia','SAR','Asia/Riyadh'],
  ['SE','Sweden','SEK','Europe/Stockholm'],
  ['SG','Singapore','SGD','Asia/Singapore'],
  ['TH','Thailand','THB','Asia/Bangkok'],
  ['TR','Türkiye','TRY','Europe/Istanbul'],
  ['UA','Ukraine','UAH','Europe/Kyiv'],
  ['US','United States','USD','America/New_York',['America/New_York','America/Chicago','America/Denver','America/Phoenix','America/Los_Angeles','America/Anchorage','Pacific/Honolulu']],
  ['VN','Vietnam','VND','Asia/Ho_Chi_Minh'],
  ['ZA','South Africa','ZAR','Africa/Johannesburg'],
];

// 🔴 ÜÇ KESİRLİ HANELİ PARA BİRİMLERİ BİLEREK YOK.
// Çıkarılanlar: BH (BHD) · JO (JOD) · KW (KWD) · OM (OMR) · TN (TND).
// ISO 4217 minor unit'leri 3, iki değil. `channex-worker`'daki fiyat çarpanı
// yalnız ZERO_DECIMAL listesini tanıyor; 3 haneli için karşılığı YOK, yani
// Kuveytli bir otel kaydolsa Channex'e giden fiyat 10 KAT yanlış olurdu.
// ⚠️ GERİ EKLEMENİN ÖN KOŞULU: çarpanın 3 haneli para birimlerini öğrenmesi
//    (Channex turu). O yapılmadan bu beş ülke buraya geri KONMAMALI.
// 📌 Zero-decimal olanlar (JP/JPY, KR/KRW, VN/VND, CL/CLP) KALDI — o yol zaten
//    kurulu ve çarpan onları tanıyor.
//
// Listede olmayan bir ülke seçilirse (Other) düşülecek yedek.
const FALLBACK_CURRENCY = 'USD';


var TZ_SET = new Set();
var CURRENCY_SET = new Set();

function browserTimeZone() {
  try { return Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch (_) { return ''; }
}
// Saat dilimi listesi tarayıcının kendi ICU verisinden gelir — kütüphane YOK.
function allTimeZones() {
  try {
    if (typeof Intl.supportedValuesOf === 'function') {
      var list = Intl.supportedValuesOf('timeZone');
      if (list && list.length) return list;
    }
  } catch (_) { /* yedeğe düş */ }
  var set = new Set();
  COUNTRIES.forEach(function (c) { set.add(c[3]); (c[4] || []).forEach(function (z) { set.add(z); }); });
  set.add('UTC');
  return Array.from(set).sort();
}
function fillSelect(el, values) {
  var frag = d.createDocumentFragment();
  values.forEach(function (v) { var o = d.createElement('option'); o.value = v; o.textContent = v; frag.appendChild(o); });
  el.appendChild(frag);
}
function initLocaleFields() {
  var countrySel = d.getElementById('country'), currencySel = d.getElementById('currency'), tzSel = d.getElementById('timezone');
  COUNTRIES.forEach(function (c) { var o = d.createElement('option'); o.value = c[0]; o.textContent = c[1]; countrySel.appendChild(o); });
  var other = d.createElement('option'); other.value = '__OTHER__'; other.textContent = tr('other'); countrySel.appendChild(other);
  // Para birimi seçenekleri YALNIZ tablodan türer; sunucu da aynı kümeyi türetiyor.
  var currencies = Array.from(new Set(COUNTRIES.map(function (c) { return c[2]; }))).sort();
  fillSelect(currencySel, currencies);
  currencySel.value = FALLBACK_CURRENCY;
  var zones = allTimeZones();
  fillSelect(tzSel, zones);
  TZ_SET = new Set(zones); CURRENCY_SET = new Set(currencies);
  var guess = browserTimeZone();
  tzSel.value = (guess && TZ_SET.has(guess)) ? guess : (TZ_SET.has('UTC') ? 'UTC' : zones[0]);
}
function onCountryChange() {
  var code = d.getElementById('country').value, otherInput = d.getElementById('countryOther');
  otherInput.hidden = code !== '__OTHER__';
  otherInput.required = code === '__OTHER__';
  clearError('locale-error', ['country', 'countryOther', 'currency', 'timezone']);
  if (!code || code === '__OTHER__') return;
  var row = COUNTRIES.find(function (c) { return c[0] === code; });
  if (!row) return;
  if (CURRENCY_SET.has(row[2])) d.getElementById('currency').value = row[2];
  // Tarayıcı tahmini bu ülkenin zonlarından biriyse KORU; değilse ülkenin varsayılanı.
  var guess = browserTimeZone(), zones = row[4] || [row[3]];
  var target = (guess && zones.indexOf(guess) !== -1) ? guess : row[3];
  if (TZ_SET.has(target)) d.getElementById('timezone').value = target;
}

// ── hata gösterimi (O8: aria-describedby + aria-invalid; O1: çevrilmiş metin)
function showError(boxId, msg, fieldIds) {
  var box = d.getElementById(boxId);
  box.textContent = msg; box.hidden = false;
  (fieldIds || []).forEach(function (id) { var f = d.getElementById(id); if (f) f.setAttribute('aria-invalid', 'true'); });
  var first = fieldIds && fieldIds[0] && d.getElementById(fieldIds[0]);
  if (first && first.focus) { first.focus({ preventScroll: true }); first.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
}
function clearError(boxId, fieldIds) {
  var box = d.getElementById(boxId); if (box) { box.hidden = true; box.textContent = ''; }
  (fieldIds || []).forEach(function (id) { var f = d.getElementById(id); if (f) f.removeAttribute('aria-invalid'); });
}

// Sunucu `code` → çevrilmiş metin (O1). Ham İngilizce `message` ASLA gösterilmez.
var SERVER_CODES = {
  invalid_email: ['e_email', 'email'], invalid_hotel_name: ['srv_hotel', 'hotelName'],
  invalid_plan: ['srv_plan'], invalid_billing: ['srv_billing'], invalid_rooms: ['srv_rooms', 'rooms'],
  invalid_country: ['e_country', 'country'], invalid_currency: ['e_currency', 'currency'],
  invalid_timezone: ['e_tz', 'timezone'], rate_limited: ['srv_rate']
};
function serverMessage(data, planId) {
  var c = data && data.code;
  if (c === 'rooms_exceed_plan') return { msg: tr('r_' + planId), field: 'rooms' };
  var m = c && SERVER_CODES[c];
  if (m) return { msg: tr(m[0]), field: m[1] };
  return { msg: tr('e_checkout') };
}

function validateRooms(planId, rooms) {
  var p = P()[planId];
  if (p && parseInt(rooms, 10) > p.rooms) return tr('r_' + planId);
  return null;
}

// GA4 olayları (consent.js; yalnız GA4_ID doluyken ve izin verildiyse). Parametrelerde kişisel veri YOK:
// yalnız plan, faturalama dönemi, hata alanı adı. cb verilirse gönderim bitince (en geç ~0,9 sn) çağrılır.
function track(n, p) {
  if (typeof window.hostlioTrack === 'function') { try { window.hostlioTrack(n, p); } catch (e) {} }
}
// Stripe'a yönlendirmeden hemen önceki olaylar: dönüş sayfasında gönderilir (consent.js, hostlioTrack.defer)
function trackLater(n, p) {
  if (window.hostlioTrack && typeof window.hostlioTrack.defer === 'function') { try { window.hostlioTrack.defer(n, p); } catch (e) {} }
}

var submitting = false;
function submitForm(ev) {
  if (ev) ev.preventDefault();
  if (submitting) return;              // çift tıklama koruması
  var form = d.getElementById('signup-form'), btn = d.getElementById('submit-btn');
  clearError('error-msg', ['firstName', 'lastName', 'email', 'hotelName']);
  clearError('rooms-error', ['rooms']);
  clearError('locale-error', ['country', 'countryOther', 'currency', 'timezone']);
  var g = function (id) { return d.getElementById(id).value.trim(); };
  var firstName = g('firstName'), lastName = g('lastName'), email = g('email'), hotelName = g('hotelName'), rooms = g('rooms'), phone = g('phone');
  var planChecked = d.querySelector('input[name="plan"]:checked');
  var planId = planChecked ? planChecked.value : 'starter';
  var countrySel = d.getElementById('country').value;
  var country = countrySel === '__OTHER__' ? g('countryOther').toUpperCase() : countrySel;
  var currency = d.getElementById('currency').value, timezone = d.getElementById('timezone').value;

  var missing = ['firstName', 'lastName', 'email', 'hotelName'].filter(function (id) { return !g(id); });
  if (missing.length) return showError('error-msg', tr('e_required'), missing);
  if (!rooms || !(parseInt(rooms, 10) >= 1)) return showError('rooms-error', tr('srv_rooms'), ['rooms']);
  if (!country || !/^[A-Z]{2}$/.test(country)) {
    return showError('locale-error', countrySel === '__OTHER__' ? tr('e_code') : tr('e_country'), [countrySel === '__OTHER__' ? 'countryOther' : 'country']);
  }
  if (!currency || !/^[A-Z]{3}$/.test(currency)) return showError('locale-error', tr('e_currency'), ['currency']);
  if (!timezone) return showError('locale-error', tr('e_tz'), ['timezone']);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return showError('error-msg', tr('e_email'), ['email']);
  var roomError = validateRooms(planId, rooms);
  if (roomError) return showError('rooms-error', roomError, ['rooms']);
  if (form && form.checkValidity && !form.checkValidity()) { form.reportValidity(); return; }

  submitting = true;
  var ev = { plan: planId, billing: isAnnual ? 'annual' : 'monthly' };
  btn.disabled = true;
  var originalLabel = btn.textContent;
  btn.textContent = tr('starting');
  var redirected = false;
  var body = Object.assign({
    firstName: firstName, lastName: lastName, email: email, hotelName: hotelName,
    rooms: parseInt(rooms, 10), phone: phone, plan: planId, billing: isAnnual ? 'annual' : 'monthly',
    country: country, currency: currency, timezone: timezone, lang: CO.lang
  // A2 — pazarlama kaynağı (ilk temas). attribution.js yoksa {} ve kayıt yine çalışır.
  }, (typeof window.hostlioAcq === 'function' && window.hostlioAcq()) || {});

  fetch(SIGNUP_CHECKOUT_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
    .then(function (res) {
      return res.json().catch(function () { return null; }).then(function (data) {
        if (res.ok && data && data.url) {
          redirected = true;
          trackLater('signup_submit', ev); trackLater('begin_checkout', ev);
          window.location.href = data.url;
          return;
        }
        // Sessiz başarısızlık BIRAKMA: sunucu 4xx/5xx döndü ya da url gelmedi.
        var e = serverMessage(data, planId);
        track('signup_submit', ev); track('signup_error', { plan: planId, error_field: e.field || 'general' });
        if (e.field === 'rooms') showError('rooms-error', e.msg, ['rooms']);
        else showError('error-msg', e.msg, e.field ? [e.field] : []);
      });
    })
    .catch(function () { showError('error-msg', tr('e_network')); track('signup_submit', ev); track('signup_error', { plan: planId, error_field: 'network' }); })
    .then(function () {
      if (!redirected) { submitting = false; btn.disabled = false; btn.textContent = originalLabel; }
    });
}

// ── arayüz: dil, plan özeti, aylık/yıllık
var FOOT = { en: ['Terms of Service', 'Privacy Policy'], tr: ['Kullanım Şartları', 'Gizlilik Politikası'], es: ['Términos del servicio', 'Política de privacidad'], it: ['Termini di servizio', 'Informativa sulla privacy'], pt: ['Termos de serviço', 'Política de privacidade'], fr: ["Conditions d’utilisation", 'Politique de confidentialité'] };
function planId() { var c = d.querySelector('input[name="plan"]:checked'); return c ? c.value : 'starter'; }
function renderPrices() {
  var suffix = isAnnual ? tr('mo_ann') : tr('mo');
  d.querySelectorAll('.plan-option').forEach(function (o) {
    var id = o.querySelector('input').value, p = P()[id];
    var pr = o.querySelector('.plan-price'); pr.textContent = money(priceOf(id));
    var sm = d.createElement('small'); sm.textContent = suffix; pr.appendChild(sm);
    var old = o.querySelector('.plan-old');
    old.hidden = !eb();
    old.querySelector('[data-t="regular"]').textContent = tr('regular');
    old.querySelector('s').textContent = money(p.r);
  });
  d.querySelectorAll('[data-eb]').forEach(function (n) { n.hidden = !eb(); });
  summary();
}
function summary() {
  var id = planId(), pt = (CO.PLAN_TXT[CO.lang] || CO.PLAN_TXT.en)[id], p = P()[id];
  d.getElementById('sum-name').textContent = p.name;
  d.getElementById('sum-price').textContent = money(priceOf(id));
  d.getElementById('sum-suffix').textContent = isAnnual ? tr('mo_ann') : tr('mo');
  var tot = d.getElementById('sum-total');
  tot.textContent = isAnnual ? tr('ann_total').replace('{at}', money(p.a)) : '';
  tot.hidden = !isAnnual;
  var ul = d.getElementById('sum-feats'), chk = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 10.5l4 4 8-9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  ul.innerHTML = '';
  (pt ? pt[1] : []).forEach(function (f) { var li = d.createElement('li'); li.innerHTML = chk; var s = d.createElement('span'); s.textContent = f; li.appendChild(s); ul.appendChild(li); });
}
function apply() {
  var l = CO.lang; d.documentElement.lang = l === 'pt' ? 'pt-BR' : l;
  if (!CO.fixed) {
    d.title = tr('title');   // Q15: kök /signup/ dil algılayınca sekme başlığı da çevrilir
    d.querySelectorAll('[data-t]').forEach(function (el) { el.textContent = tr(el.getAttribute('data-t')); });
    d.querySelectorAll('[data-tph]').forEach(function (el) { el.placeholder = tr(el.getAttribute('data-tph')); });
    var t = d.getElementById('co-terms'); if (t) t.innerHTML = tr('terms').replace('{t}', CO.TERMS[l]).replace('{p}', CO.PRIVACY[l]);
    var ft = d.getElementById('co-f-terms'), fp = d.getElementById('co-f-privacy'), f = FOOT[l] || FOOT.en;
    if (ft) { ft.textContent = f[0]; ft.href = CO.TERMS[l]; } if (fp) { fp.textContent = f[1]; fp.href = CO.PRIVACY[l]; }
    d.querySelectorAll('[data-home]').forEach(function (a) { a.href = CO.HOME[l]; });
    var b = d.getElementById('submit-btn'); if (b && !b.disabled) b.textContent = tr('submit');
    var o = d.querySelector('#country option[value="__OTHER__"]'); if (o) o.textContent = tr('other');
  }
  var sel = d.getElementById('co-lang'); if (sel) sel.value = l;
  renderPrices();
}
function setBill(a) {
  isAnnual = a;
  d.querySelectorAll('.co-billing [data-bill]').forEach(function (x) { var on = (x.dataset.bill === 'a') === a; x.classList.toggle('on', on); x.setAttribute('aria-pressed', on); });
  renderPrices();
}

d.addEventListener('DOMContentLoaded', function () {
  initLocaleFields();
  var q = new URLSearchParams(location.search), p = q.get('plan');
  if (p && d.getElementById('plan-' + p)) d.getElementById('plan-' + p).checked = true;
  apply();
  if (q.get('billing') === 'annual') setBill(true);
  d.querySelectorAll('input[name="plan"]').forEach(function (r) { r.addEventListener('change', function () { summary(); clearError('rooms-error', ['rooms']); track('signup_plan_select', { plan: r.value }); }); });
  d.querySelectorAll('.co-billing [data-bill]').forEach(function (x) { x.addEventListener('click', function () { setBill(x.dataset.bill === 'a'); track('pricing_billing_toggle', { billing: isAnnual ? 'annual' : 'monthly', context: 'signup' }); }); });
  // kayıt adımı 1: forma ilk dokunuş (alan içeriği gönderilmez)
  var sf = d.getElementById('signup-form'), started = false;
  sf.addEventListener('focusin', function () { if (started) return; started = true; track('signup_form_start', { plan: planId(), billing: isAnnual ? 'annual' : 'monthly' }); });
  d.getElementById('signup-form').addEventListener('submit', submitForm);
  d.getElementById('rooms').addEventListener('input', function () { clearError('rooms-error', ['rooms']); });
  d.getElementById('country').addEventListener('change', onCountryChange);
  d.querySelectorAll('#signup-form input, #signup-form select').forEach(function (f) {
    f.addEventListener('invalid', function () { f.setAttribute('aria-invalid', 'true'); });
    f.addEventListener('input', function () { if (f.validity && f.validity.valid) f.removeAttribute('aria-invalid'); });
  });
  var sel = d.getElementById('co-lang');
  if (sel) sel.addEventListener('change', function () {
    try { localStorage.setItem('hostlio_lang', sel.value); } catch (e) {}
    var u = new URL(location.href);
    if (CO.fixed) { u.pathname = CO.SIGNUP[sel.value]; u.searchParams.delete('lang'); location.href = u.pathname + u.search; return; }
    CO.lang = sel.value; u.searchParams.set('lang', sel.value); history.replaceState(null, '', u); apply();
  });
  if (HP) HP.onUpdate(renderPrices);   // canlı fiyat + early_bird bayrağı (Y2)

  // Stripe dönüşü: ?checkout=success|cancelled
  var status = q.get('checkout'), msg = d.getElementById('error-msg');
  if (status === 'success') {
    track('sign_up', { method: 'stripe_checkout' });
    var fw = d.getElementById('signup-form'); if (fw) fw.hidden = true;
    msg.classList.add('co-ok'); msg.textContent = tr('ok_paid'); msg.hidden = false;
  } else if (status === 'cancelled') {
    track('checkout_cancelled', {});
    msg.textContent = tr('cancelled'); msg.hidden = false;
  }
  d.documentElement.classList.remove('nojs'); d.documentElement.classList.add('js');
});
})();
