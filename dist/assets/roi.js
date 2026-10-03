// ROI hesaplayıcı (/xx/roi-calculator/). Satır içi betik yerine dosya (O4).
// O2: plan önerisi oda limitine VE aylık AI yanıt kotasına göre yapılır; kotayı aşan
// kısım ayrıca belirtilir ve tasarruf kotayla sınırlanır (Lio sınırda otomatik yanıtı durdurur).
// Fiyat/kota/oda limiti: pricing.py → prices.js (window.HostlioPrices), canlı fiyatla tazelenir.
(function () {
  var f = document.getElementById('roi-form'), HP = window.HostlioPrices;
  if (!f || !HP) return;
  f.addEventListener('submit', function (e) { e.preventDefault(); });
  var C = HP.config, ds = f.dataset, ORDER = ['starter', 'pro', 'growth'];
  var $ = function (n) { return HP.money(Math.round(n)); };
  function hrsFmt(h) { var x = Math.round(h * 10) / 10, i = Math.floor(x), dec = Math.round((x - i) * 10);
    return HP.number(i, C.lang) + (dec ? ((C.lang === 'en') ? '.' : ',') + dec : ''); }
  function v(n) { var x = parseFloat(f.elements[n].value); return isFinite(x) && x >= 0 ? x : 0; }
  function el(id) { return document.getElementById(id); }
  function calc() {
    var rooms = v('rooms'), m = v('msgs') * 30, share = Math.min(v('share'), 100) / 100, night = Math.min(v('night'), 100) / 100;
    var need = Math.round(m * share), plan = null, over = 0, id;
    // oda limitine uyan en küçük plan; içlerinden kotası yetenin ilki, yoksa en büyük uygun plan
    var fits = ORDER.filter(function (k) { return C.plans[k] && rooms <= C.plans[k].rooms; });
    for (var i = 0; i < fits.length; i++) { if (need <= C.plans[fits[i]].quota) { id = fits[i]; break; } }
    if (!id && fits.length) { id = fits[fits.length - 1]; over = need - C.plans[id].quota; }
    plan = id ? C.plans[id] : null;
    var auto = plan ? Math.min(need, plan.quota) : need;   // kota üstü otomatik yanıtlanmaz
    var hrs = auto * v('min') / 60, cost = hrs * v('cost');
    el('roi-hours').textContent = hrsFmt(hrs) + ' ' + ds.h;
    el('roi-cost').textContent = $(cost) + ds.perMo;
    el('roi-night').textContent = HP.number(Math.round(auto * night), C.lang) + ' ' + ds.msgs;
    el('roi-ai').textContent = HP.number(need, C.lang) + ' ' + ds.msgs;
    el('roi-plan').textContent = plan ? plan.name + ' · ' + $(plan.m) + ds.perMo : ds.over;
    el('roi-net').textContent = plan ? $(cost - plan.m) + ds.perMo : '–';
    var q = el('roi-quota');
    q.hidden = !(plan && over > 0);
    if (plan && over > 0) q.textContent = ds.quotaOver.replace('{n}', HP.number(over, C.lang)).replace('{plan}', plan.name).replace('{q}', HP.number(plan.quota, C.lang));
  }
  f.addEventListener('input', calc);
  HP.onUpdate(calc);
  calc();
})();
