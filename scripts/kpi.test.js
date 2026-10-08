// node scripts/kpi.test.js — RevPAR/ADR/doluluk ve OTA komisyon formüllerinin birim testleri
const assert = require('assert');
const K = require('../src/assets/kpi.js');
let n = 0;
function t(name, fn) { fn(); n++; console.log('ok', name); }
const close = (a, b, eps = 1e-9) => assert.ok(Math.abs(a - b) < eps, `${a} != ${b}`);

t('available = rooms × days', () => { assert.strictEqual(K.available(20, 30), 600); assert.ok(isNaN(K.available(-1, 30))); assert.ok(isNaN(K.available('', 30))); });
t('occupancy', () => { close(K.occupancy(450, 600), 0.75); assert.ok(isNaN(K.occupancy(10, 0))); });
t('adr', () => { close(K.adr(45000, 450), 100); assert.ok(isNaN(K.adr(45000, 0))); });
t('revpar', () => { close(K.revpar(45000, 600), 75); assert.ok(isNaN(K.revpar(100, 0))); });
t('revpar = adr × occupancy', () => {
  const k = K.kpis(20, 30, 450, 45000);
  close(k.revpar, k.adr * k.occupancy); close(K.revparFrom(100, 0.75), 75);
});
t('page example (TR/EN): 12 rooms, 31 days, 285 sold, 39,900 revenue', () => {
  const k = K.kpis(12, 31, 285, 39900);
  assert.strictEqual(k.available, 372); close(k.occupancy, 285 / 372); close(k.adr, 140); close(k.revpar, 39900 / 372);
  assert.strictEqual(Math.round(k.occupancy * 1000) / 10, 76.6); assert.strictEqual(Math.round(k.revpar * 100) / 100, 107.26);
});
t('warn when sold > available', () => { assert.strictEqual(K.kpis(10, 1, 11, 100).warn, true); assert.strictEqual(K.kpis(10, 1, 10, 100).warn, false); });
t('comma decimal input', () => { close(K.adr('1500,5', 10), 150.05); });
t('commission', () => {
  const r = K.commission(1000, 15, 2, 4);
  close(r.commission, 150); close(r.fees, 20); close(r.net, 830); close(r.kept, 0.83); close(r.netNight, 207.5);
});
t('commission: fee optional, nights optional', () => {
  const r = K.commission(200, 18, '', ''); close(r.net, 164); assert.ok(isNaN(r.netNight));
});
t('commission example on page: 1,200 gross, 18%, 1.5%, 3 nights', () => {
  const r = K.commission(1200, 18, 1.5, 3); close(r.commission, 216); close(r.fees, 18); close(r.net, 966); close(r.netNight, 322);
});
t('commission invalid', () => { assert.ok(isNaN(K.commission('', 15).net)); assert.ok(isNaN(K.commission(100, -2).net)); });
console.log(`\n${n} tests passed`);
