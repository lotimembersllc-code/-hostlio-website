// tasarim-v2: eski signup.html betiği — MANTIK DEĞİŞMEDİ, yalnız metinler tr() ile 6 dile bağlandı.
// tr() ve dil seçimi: signup_page.py içindeki window.CO bloğu + /assets/checkout.js.
// Sunucu tarafı Checkout Session üreten edge function. Fiyat/plan doğrulaması
// SUNUCUDA yapılır; buradaki istemci kontrolleri yalnız ilk savunma katmanı.
const SIGNUP_CHECKOUT_URL = 'https://brzetctpyaxognnvjrnd.supabase.co/functions/v1/signup-checkout';
let submitting = false;
let isAnnual = false;
const monthlyPrices = { starter: 49, pro: 89, growth: 149 };
const annualPrices = { starter: 39, pro: 71, growth: 119 };
const monthlyOld = { starter: 59, pro: 109, growth: 189 };
const annualOld = { starter: 59, pro: 109, growth: 189 };

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

// Seçeneklerin üyelik kümeleri — initLocaleFields() dolduruyor.
let TZ_SET = new Set();
let CURRENCY_SET = new Set();

// Tarayıcının tahmini — ülke seçilmeden önceki ilk değer.
function browserTimeZone() {
  try { return Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch (_) { return ''; }
}

// Saat dilimi listesi tarayıcının kendi ICU verisinden gelir — kütüphane YOK.
// Desteklemeyen eski tarayıcılar için tablodaki zonlara düşülür.
function allTimeZones() {
  try {
    if (typeof Intl.supportedValuesOf === 'function') {
      const list = Intl.supportedValuesOf('timeZone');
      if (list && list.length) return list;
    }
  } catch (_) { /* aşağıdaki yedeğe düş */ }
  const set = new Set();
  COUNTRIES.forEach(function (c) {
    set.add(c[3]);
    (c[4] || []).forEach(function (z) { set.add(z); });
  });
  set.add('UTC');
  return Array.from(set).sort();
}

function fillSelect(el, values, labelFn) {
  const frag = document.createDocumentFragment();
  values.forEach(function (v) {
    const o = document.createElement('option');
    o.value = v;
    o.textContent = labelFn ? labelFn(v) : v;
    frag.appendChild(o);
  });
  el.appendChild(frag);
}

function initLocaleFields() {
  const countrySel = document.getElementById('country');
  const currencySel = document.getElementById('currency');
  const tzSel = document.getElementById('timezone');

  COUNTRIES.forEach(function (c) {
    const o = document.createElement('option');
    o.value = c[0];
    o.textContent = c[1];
    countrySel.appendChild(o);
  });
  const other = document.createElement('option');
  other.value = '__OTHER__';
  other.textContent = tr('other');
  countrySel.appendChild(other);

  // Para birimi seçenekleri YALNIZ tablodan türer — ayrı elle yazılmış liste
  // tutulmuyor. Sunucu (signup-checkout) da aynı kümeyi türetiyor, böylece
  // istemcinin sunduğu ile sunucunun kabul ettiği BİREBİR aynı oluyor.
  const currencies = Array.from(new Set(
    COUNTRIES.map(function (c) { return c[2]; })
  )).sort();
  fillSelect(currencySel, currencies);
  currencySel.value = FALLBACK_CURRENCY;

  const zones = allTimeZones();
  fillSelect(tzSel, zones);
  TZ_SET = new Set(zones);
  CURRENCY_SET = new Set(currencies);

  const guess = browserTimeZone();
  tzSel.value = (guess && TZ_SET.has(guess)) ? guess
              : (TZ_SET.has('UTC') ? 'UTC' : zones[0]);
}

function onCountryChange() {
  const code = document.getElementById('country').value;
  const otherInput = document.getElementById('countryOther');
  otherInput.style.display = code === '__OTHER__' ? 'block' : 'none';
  if (!code || code === '__OTHER__') return;

  const row = COUNTRIES.find(function (c) { return c[0] === code; });
  if (!row) return;

  const currencySel = document.getElementById('currency');
  const tzSel = document.getElementById('timezone');

  if (CURRENCY_SET.has(row[2])) currencySel.value = row[2];

  // Tarayıcı tahmini bu ülkenin zonlarından biriyse KORU; değilse ülkenin
  // varsayılanına geç. İkisi de "ülke seçimi geçersiz kılar" kuralına uyuyor —
  // ülke kapsamı belirliyor, kapsam içindeyse daha isabetli olan tahmin kalıyor.
  const guess = browserTimeZone();
  const zones = row[4] || [row[3]];
  const target = (guess && zones.indexOf(guess) !== -1) ? guess : row[3];
  if (TZ_SET.has(target)) tzSel.value = target;
}

function toggleBilling() {
  isAnnual = !isAnnual;
  const toggle = document.getElementById('billing-toggle');
  const dot = document.getElementById('toggle-dot');
  if (toggle) toggle.style.background = isAnnual ? 'var(--orange)' : 'var(--gray-200)';
  if (dot) dot.style.transform = isAnnual ? 'translateX(18px)' : 'translateX(0)';
  
  const prices = isAnnual ? annualPrices : monthlyPrices;
  const oldPrices = isAnnual ? annualOld : monthlyOld;
  const suffix = isAnnual ? tr('mo_ann') : tr('mo');
  
  ['starter', 'pro', 'growth'].forEach(plan => {
    const label = document.querySelector(`#plan-${plan} + label`);
    if (label) {
      label.querySelector('.plan-price').innerHTML = '$' + prices[plan] + '<small>' + suffix + '</small>';
      label.querySelector('.plan-old').innerHTML = tr('regular') + ' <s>$' + oldPrices[plan] + '</s>';
    }
    const input = document.getElementById('plan-' + plan);
    const planNames = { starter: 'Starter', pro: 'Pro', growth: 'Growth' };
    if (input) input.value = planNames[plan] + ' - Early Bird (' + (isAnnual ? 'Annual' : 'Monthly') + ' $' + prices[plan] + '/mo)';
  });
}

// (6 hard-coded Payment Link SİLİNDİ — checkout artık signup-checkout üzerinden
//  sunucu tarafında oluşturuluyor.)

function clearRoomError() {
  document.getElementById('rooms').style.borderColor = '';
  const e = document.getElementById('rooms-error');
  if (e) e.style.display = 'none';
}

function validateRooms(planId, rooms) {
  // starter 15 → 10 (2026-08-10): aşağıdaki mesaj zaten "up to 10 rooms" diyordu,
  // limit 15'ti. Sunucu tarafı kopyası: signup-checkout/index.ts ROOM_LIMITS.
  const limits = { starter: 10, pro: 50, growth: 150 };
  const messages = {
    starter: tr('r_starter'),
    pro: tr('r_pro'),
    growth: tr('r_growth')
  };
  if (limits[planId] && parseInt(rooms) > limits[planId]) return messages[planId];
  return null;
}

async function submitForm() {
  if (submitting) return;            // çift tıklama koruması
  const btn = document.getElementById('submit-btn');
  const errorMsg = document.getElementById('error-msg');
  const roomsInput = document.getElementById('rooms');
  const roomsError = document.getElementById('rooms-error');
  errorMsg.style.display = 'none';
  clearRoomError();

  const firstName = document.getElementById('firstName').value.trim();
  const lastName = document.getElementById('lastName').value.trim();
  const email = document.getElementById('email').value.trim();
  const hotelName = document.getElementById('hotelName').value.trim();
  const rooms = roomsInput.value.trim();
  const phone = document.getElementById('phone').value.trim();
  const planChecked = document.querySelector('input[name="plan"]:checked');
  const planId = planChecked.id.replace('plan-', '');

  // Ülke / para birimi / saat dilimi — üçü de zorunlu.
  const localeError = document.getElementById('locale-error');
  localeError.style.display = 'none';
  const countrySel = document.getElementById('country').value;
  const country = countrySel === '__OTHER__'
    ? document.getElementById('countryOther').value.trim().toUpperCase()
    : countrySel;
  const currency = document.getElementById('currency').value;
  const timezone = document.getElementById('timezone').value;

  if (!firstName || !lastName || !email || !hotelName || !rooms) {
    errorMsg.textContent = tr('e_required');
    errorMsg.style.display = 'block';
    return;
  }

  if (!country || !/^[A-Z]{2}$/.test(country)) {
    localeError.textContent = countrySel === '__OTHER__'
      ? tr('e_code')
      : tr('e_country');
    localeError.style.display = 'block';
    document.getElementById('country').scrollIntoView({ behavior: 'smooth', block: 'center' });
    return;
  }
  if (!currency || !/^[A-Z]{3}$/.test(currency)) {
    localeError.textContent = tr('e_currency');
    localeError.style.display = 'block';
    return;
  }
  if (!timezone) {
    localeError.textContent = tr('e_tz');
    localeError.style.display = 'block';
    return;
  }

  if (!email.includes('@')) {
    errorMsg.textContent = tr('e_email');
    errorMsg.style.display = 'block';
    return;
  }

  const roomError = validateRooms(planId, rooms);
  if (roomError) {
    roomsInput.style.borderColor = '#dc3545';
    roomsError.textContent = roomError;
    roomsError.style.display = 'block';
    roomsInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
    return;
  }

  const billing = isAnnual ? 'annual' : 'monthly';

  submitting = true;
  btn.disabled = true;
  const originalLabel = btn.textContent;
  btn.textContent = tr('starting');
  let redirected = false;

  // Sunucu tarafı Checkout Session — plan ADI değil, temiz planId gönderilir.
  // client_reference_id GÖNDERİLMEZ (hesap henüz yok).
  try {
    const res = await fetch(SIGNUP_CHECKOUT_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(Object.assign({
        firstName, lastName, email, hotelName,
        rooms: parseInt(rooms, 10),
        phone, plan: planId, billing,
        country, currency, timezone
      // A2 — pazarlama kaynağı (ilk temas). attribution.js yüklenmediyse ya da
      // depolama engelliyse `null` döner ve gövde ESKİSİ GİBİ gider: ölçüm
      // kaybolur, kayıt akışı bozulmaz.
      }, (typeof window.hostlioAcq === 'function' && window.hostlioAcq()) || {}))
    });

    let data = null;
    try { data = await res.json(); } catch (_) { /* gövde yok/parse edilemedi */ }

    if (res.ok && data && data.url) {
      redirected = true;
      window.location.href = data.url;   // Stripe Checkout'a git — buton kilitli kalır
      return;
    }

    // 🔴 Sessiz başarısızlık BIRAKMA: sunucu 400/500 döndü ya da url gelmedi.
    errorMsg.textContent = (data && data.message)
      ? data.message
      : tr('e_checkout');
    errorMsg.style.display = 'block';
  } catch (_e) {
    // Ağ hatası / fonksiyona ulaşılamadı.
    errorMsg.textContent = tr('e_network');
    errorMsg.style.display = 'block';
  } finally {
    // Yalnız yönlendirme OLMADIYSA butonu geri aç (aksi hâlde sayfa değişiyor).
    if (!redirected) {
      submitting = false;
      btn.disabled = false;
      btn.textContent = originalLabel;
    }
  }
}

// Checkout dönüşü: success_url/cancel_url ?checkout=... ile bu sayfaya döner.
document.addEventListener('DOMContentLoaded', function () {
  initLocaleFields();

  const status = new URLSearchParams(window.location.search).get('checkout');
  if (!status) return;
  const errorMsg = document.getElementById('error-msg');
  if (!errorMsg) return;
  if (status === 'success') {
    errorMsg.style.color = '#198754';
    errorMsg.textContent = tr('ok_paid');
    errorMsg.style.display = 'block';
  } else if (status === 'cancelled') {
    errorMsg.textContent = tr('cancelled');
    errorMsg.style.display = 'block';
  }
});
