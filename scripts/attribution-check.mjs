// A2 KAPISI — İLK TEMAS MODELİNİ ÖLÇÜYE ÇEVİRİR (`attribution.js`).
//
// 🔑 KURAL: ilk temas ÜZERİNE YAZILAMAZ. Bu dosyanın var olma sebebi tek bir
// arıza sınıfı: modelin sessizce "son temas"a dönmesi. O hâlde reklamdan
// blog yazısına düşüp günler sonra doğrudan kaydolan ziyaretçi 'direct'
// sayılır, reklam BEDAVA görünür ve bütçe kararı yanlış verilir. Hiçbir
// hata mesajı çıkmaz — sayılar makul görünmeye devam eder.
//
// Koşturma:  node scripts/attribution-check.mjs
// (kardeşi: scripts/i18n-check.mjs)

import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert';

const SRC = fs.readFileSync(new URL('../attribution.js', import.meta.url), 'utf8');

function makeStore(broken = false) {
  const m = new Map();
  return {
    getItem: k => { if (broken) throw new Error('blocked'); return m.has(k) ? m.get(k) : null; },
    setItem: (k, v) => { if (broken) throw new Error('blocked'); m.set(k, v); },
  };
}

// Bir "sayfa yüklemesi": aynı localStorage, yeni pencere.
function visit(store, { path = '/', search = '', referrer = '', host = 'hostliopro.com' } = {}) {
  const win = {
    location: { search, pathname: path, hostname: host },
    localStorage: store,
  };
  const ctx = vm.createContext({ window: win, document: { referrer }, URL, URLSearchParams, Date, JSON, console });
  ctx.globalThis = ctx;
  vm.runInContext(SRC, ctx);
  return win.hostlioAcq();
}

let n = 0; const ok = (msg) => { n++; console.log('  ✓', msg); };

// 1 — reklamdan blog yazısına düşüş
const s1 = makeStore();
let r = visit(s1, { path: '/blog/how-to-reduce-hotel-no-shows.html', search: '?utm_source=google&utm_medium=cpc&utm_campaign=kis2026&gclid=ABC123', referrer: 'https://www.google.com/' });
assert.equal(r.acq_source, 'google');
assert.equal(r.acq_medium, 'cpc');
assert.equal(r.acq_campaign, 'kis2026');
assert.equal(r.acq_click_id, 'gclid:ABC123');
assert.equal(r.acq_landing, '/blog/how-to-reduce-hotel-no-shows.html');
ok('reklam → blog yazısı: kaynak, kampanya, tıklama kimliği ve iniş sayfası yakalandı');

// 2 — ILK TEMAS KAZANIR: gunler sonra dogrudan /signup
r = visit(s1, { path: '/signup.html' });
assert.equal(r.acq_source, 'google', 'ilk temas üzerine yazıldı!');
assert.equal(r.acq_campaign, 'kis2026');
assert.equal(r.acq_landing, '/blog/how-to-reduce-hotel-no-shows.html');
ok('ilk temas korundu: sonradan doğrudan gelen ziyaret kampanyayı SİLMİYOR');

// 3 — ikinci bir reklam da uzerine yazamaz
r = visit(s1, { path: '/', search: '?utm_source=facebook&utm_campaign=baska' });
assert.equal(r.acq_source, 'google');
ok('ikinci kampanya da ilk temasın üzerine yazmıyor');

// 4 — dis yonlendiren, utm yok
const s2 = makeStore();
r = visit(s2, { path: '/', referrer: 'https://news.ycombinator.com/item?id=1' });
assert.equal(r.acq_source, 'news.ycombinator.com');
assert.equal(r.acq_medium, 'referral');
assert.equal(r.acq_referrer, 'news.ycombinator.com');
ok('utm yokken yönlendiren host kaynak oluyor (tam URL SAKLANMIYOR)');

// 5 — ic gezinme yonlendiren SAYILMIYOR
const s3 = makeStore();
r = visit(s3, { path: '/signup.html', referrer: 'https://hostliopro.com/faq.html' });
assert.equal(r.acq_source, 'direct');
assert.equal(r.acq_medium, 'none');
assert.equal(r.acq_referrer, null);
ok('kendi alan adımız yönlendiren sayılmıyor → direct');

// 6 — fbclid ucretli SAYILMIYOR
const s4 = makeStore();
r = visit(s4, { path: '/', search: '?fbclid=XYZ' });
assert.equal(r.acq_source, 'facebook');
assert.equal(r.acq_medium, 'social', 'fbclid cpc sayıldı — organik paylaşım reklam hanesine yazılır!');
ok('fbclid social sayılıyor, cpc değil');

// 7 — depolama engelli: cokmuyor, sayfa ici calisiyor
const s5 = makeStore(true);
r = visit(s5, { path: '/', search: '?utm_source=bing' });
assert.equal(r.acq_source, 'bing');
ok('localStorage engelliyken çökmüyor, bellek yedeği çalışıyor');

// 8 — bozuk kayit ilk temas sayilmiyor
const s6 = makeStore(); s6.setItem('hostlio_acq', '{bozuk json');
r = visit(s6, { path: '/', search: '?utm_source=kurtarildi' });
assert.equal(r.acq_source, 'kurtarildi');
ok('bozuk localStorage kaydı ilk temas sayılmıyor, yeniden yakalanıyor');

console.log(`\n${n}/8 geçti`);
