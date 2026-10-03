// Y2/O9 — fiyatların tarayıcı tarafı. Tek kaynak pricing.py: build onu
// <script type="application/json" id="hostlio-pricing"> olarak sayfaya gömer.
// Sayfa açılınca Supabase `plans` ucundan (Stripe) canlı tutar ve early_bird
// bayrağı okunur; abone olanlar (fiyat sayfası, ödeme sayfası, ROI) yeniden çizer.
// Biçim (sembol yeri, binlik ayıracı) build'deki pricing.money() ile birebir aynı.
(function () {
  var el = document.getElementById('hostlio-pricing');
  if (!el) return;
  var C;
  try { C = JSON.parse(el.textContent); } catch (e) { return; }
  var subs = [], started = false;

  function fmt(l) { return C.fmt[l || C.lang] || C.fmt.en; }
  function number(n, l) {
    return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, fmt(l).group);
  }
  function money(n, l) { var f = fmt(l); return f.pre + number(n, l) + f.post; }

  function notify() { subs.forEach(function (f) { try { f(C); } catch (e) { /* tek abone düşerse ötekiler çalışsın */ } }); }

  function refresh() {
    if (started) return;
    started = true;
    if (!window.fetch || !C.endpoint) return;
    fetch(C.endpoint, { headers: { Authorization: 'Bearer ' + C.anon } })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (j) {
        if (!j || !Array.isArray(j.plans)) return;
        // Biçim tablosu USD için; başka para birimi gelirse statik değerler kalır.
        if (j.currency && String(j.currency).toLowerCase() !== 'usd') return;
        j.plans.forEach(function (p) {
          var d = C.plans[p.id];
          if (!d) return;
          if (p.monthly && typeof p.monthly.amount === 'number') d.m = p.monthly.amount;
          if (p.annual && typeof p.annual.amount === 'number') d.a = p.annual.amount;
        });
        if (typeof j.early_bird === 'boolean') C.early_bird = j.early_bird;
        notify();
      })
      .catch(function () { /* ağ hatası: derlemedeki fiyatlar kalır */ });
  }

  // Ortak DOM yazıcısı: data-price (kart, aylık/yıllık), data-price-m/-am/-a (tablo),
  // data-at (yıllık toplam), data-regular (normal fiyat), data-eb (Early Bird metni).
  function apply(root, annual) {
    root = root || document;
    var P = C.plans;
    root.querySelectorAll('[data-price]').forEach(function (b) {
      var v = P[b.getAttribute('data-price')]; if (!v) return;
      b.textContent = money(annual ? Math.round(v.a / 12) : v.m);
    });
    [['data-price-m', function (v) { return v.m; }], ['data-price-am', function (v) { return Math.round(v.a / 12); }],
     ['data-price-a', function (v) { return v.a; }], ['data-at', null], ['data-regular', function (v) { return v.r; }]]
      .forEach(function (x) {
        root.querySelectorAll('[' + x[0] + ']').forEach(function (n) {
          var v = P[n.getAttribute(x[0])]; if (!v) return;
          var val = x[1] ? x[1](v) : v.a;
          var t = n.querySelector('s') || n;
          t.textContent = money(val);
        });
      });
    document.querySelectorAll('[data-eb]').forEach(function (n) { n.hidden = !C.early_bird; });
  }

  window.HostlioPrices = {
    config: C, money: money, number: number, apply: apply,
    onUpdate: function (f) { subs.push(f); refresh(); }
  };
})();
