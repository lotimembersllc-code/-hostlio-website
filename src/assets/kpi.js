// Ücretsiz otel araçları: RevPAR / ADR / doluluk ve OTA komisyonu → net gelir hesaplayıcıları.
// Satır içi betik yok (CSP script-src 'self'); metinler sayfadaki data-* özniteliklerinden gelir.
// Saf hesap fonksiyonları node'da da çalışır: require('./kpi.js') → scripts/kpi.test.js
(function (root) {
  'use strict';
  function num(x) { var n = typeof x === 'number' ? x : parseFloat(String(x).replace(',', '.')); return isFinite(n) ? n : NaN; }
  function pos(x) { var n = num(x); return isFinite(n) && n >= 0 ? n : NaN; }

  var K = {
    /** Satılabilir oda gecesi = oda sayısı × gün */
    available: function (rooms, days) { var r = pos(rooms), d = pos(days); return isFinite(r) && isFinite(d) ? r * d : NaN; },
    /** Doluluk (0–1) = satılan oda gecesi ÷ satılabilir oda gecesi */
    occupancy: function (sold, available) { var s = pos(sold), a = pos(available); return isFinite(s) && a > 0 ? s / a : NaN; },
    /** ADR = oda geliri ÷ satılan oda gecesi */
    adr: function (revenue, sold) { var v = pos(revenue), s = pos(sold); return isFinite(v) && s > 0 ? v / s : NaN; },
    /** RevPAR = oda geliri ÷ satılabilir oda gecesi (= ADR × doluluk) */
    revpar: function (revenue, available) { var v = pos(revenue), a = pos(available); return isFinite(v) && a > 0 ? v / a : NaN; },
    revparFrom: function (adr, occ) { var x = pos(adr), o = pos(occ); return isFinite(x) && isFinite(o) ? x * o : NaN; },
    /** Tüm göstergeler tek seferde. warn: satılan > satılabilir */
    kpis: function (rooms, days, sold, revenue) {
      var a = K.available(rooms, days);
      return { available: a, occupancy: K.occupancy(sold, a), adr: K.adr(revenue, sold), revpar: K.revpar(revenue, a),
               warn: isFinite(a) && pos(sold) > a };
    },
    /** OTA komisyonu → net gelir. rate ve fee yüzde (15 = %15); nights isteğe bağlı (gece başı net). */
    commission: function (gross, rate, fee, nights) {
      var g = pos(gross), r = pos(rate), f = pos(fee); if (!isFinite(f)) f = 0;
      if (!isFinite(g) || !isFinite(r)) return { commission: NaN, fees: NaN, net: NaN, kept: NaN, netNight: NaN };
      var c = g * r / 100, x = g * f / 100, net = g - c - x, n = pos(nights);
      return { commission: c, fees: x, net: net, kept: g > 0 ? net / g : NaN, netNight: n > 0 ? net / n : NaN };
    }
  };
  if (typeof module === 'object' && module.exports) module.exports = K;
  if (typeof document === 'undefined') return;
  root.HostlioKPI = K;

  var LOC = { tr: 'tr-TR', en: 'en-US', es: 'es-ES', it: 'it-IT', pt: 'pt-BR', fr: 'fr-FR' };
  function fmt(lang) {
    var loc = LOC[lang] || 'en-US';
    return {
      n: function (v, d) { return isFinite(v) ? new Intl.NumberFormat(loc, { maximumFractionDigits: d == null ? 0 : d, minimumFractionDigits: 0 }).format(v) : '–'; },
      pct: function (v) { return isFinite(v) ? new Intl.NumberFormat(loc, { style: 'percent', maximumFractionDigits: 1 }).format(v) : '–'; },
      cur: function (v, c) {
        if (!isFinite(v)) return '–';
        var d = Math.abs(v - Math.round(v)) < 0.005 ? 0 : 2;
        try { return new Intl.NumberFormat(loc, { style: 'currency', currency: c, maximumFractionDigits: d, minimumFractionDigits: d }).format(v); }
        catch (e) { return new Intl.NumberFormat(loc, { maximumFractionDigits: 2 }).format(v) + ' ' + c; }
      }
    };
  }
  function el(id) { return document.getElementById(id); }
  function set(id, t) { var e = el(id); if (e) e.textContent = t; }
  function val(f, n) { return f.elements[n] ? f.elements[n].value : ''; }

  function kpiForm(f) {
    var F = fmt(f.getAttribute('data-lang')), ds = f.dataset;
    function run() {
      var c = val(f, 'currency') || 'USD', rooms = val(f, 'rooms'), days = val(f, 'days'), sold = val(f, 'sold'), rev = val(f, 'revenue');
      var k = K.kpis(rooms, days, sold, rev);
      set('kpi-avail', F.n(k.available));
      set('kpi-occ', F.pct(k.occupancy));
      set('kpi-adr', F.cur(k.adr, c));
      set('kpi-revpar', F.cur(k.revpar, c));
      set('kpi-avail-f', F.n(pos(rooms)) + ' × ' + F.n(pos(days)) + ' = ' + F.n(k.available));
      set('kpi-occ-f', F.n(pos(sold)) + ' ÷ ' + F.n(k.available) + ' = ' + F.pct(k.occupancy));
      set('kpi-adr-f', F.cur(pos(rev), c) + ' ÷ ' + F.n(pos(sold)) + ' = ' + F.cur(k.adr, c));
      set('kpi-revpar-f', F.cur(pos(rev), c) + ' ÷ ' + F.n(k.available) + ' = ' + F.cur(k.revpar, c));
      var w = el('kpi-warn'); if (w) { w.hidden = !k.warn; w.textContent = k.warn ? ds.warn : ''; }
    }
    f.addEventListener('input', run); f.addEventListener('change', run);
    f.addEventListener('submit', function (e) { e.preventDefault(); run(); });
    run();
  }
  function comForm(f) {
    var F = fmt(f.getAttribute('data-lang'));
    function run() {
      var c = val(f, 'currency') || 'USD';
      var r = K.commission(val(f, 'gross'), val(f, 'rate'), val(f, 'fee'), val(f, 'nights'));
      set('com-commission', F.cur(r.commission, c));
      set('com-fees', F.cur(r.fees, c));
      set('com-net', F.cur(r.net, c));
      set('com-kept', F.pct(r.kept));
      set('com-night', F.cur(r.netNight, c));
    }
    f.addEventListener('input', run); f.addEventListener('change', run);
    f.addEventListener('submit', function (e) { e.preventDefault(); run(); });
    run();
  }
  var a = el('kpi-form'); if (a) kpiForm(a);
  var b = el('com-form'); if (b) comForm(b);
})(typeof window !== 'undefined' ? window : this);
