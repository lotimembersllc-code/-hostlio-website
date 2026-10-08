// Sayfa başına paylaşım görseli (1200×630 JPEG) → src/assets/og/<dil>-<anahtar>.jpg
// Girdi: og/pages.json (build.py yazar). Ana sayfa dil geneli og-<dil>.png'yi kullanır, burada üretilmez.
// Çalıştırma: python3 build.py && node og/make_pages.mjs && python3 build.py
//   (playwright-core gerekir; sistem Chrome'u kullanılır. Yalnız eksik ya da başlığı değişmiş sayfalar yeniden üretilir.)
import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUT = path.join(ROOT, 'src/assets/og');
const FONT = 'file://' + path.join(ROOT, 'src/assets/fonts');
const pages = JSON.parse(fs.readFileSync(path.join(ROOT, 'og/pages.json'), 'utf8'));
const stampFile = path.join(OUT, 'stamps.json');
const stamps = fs.existsSync(stampFile) ? JSON.parse(fs.readFileSync(stampFile, 'utf8')) : {};
const BLOG = { tr: 'Blog', en: 'Blog', es: 'Blog', it: 'Blog', pt: 'Blog', fr: 'Blog' };
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const clean = t => t.replace(/\s*\|\s*Hostlio Pro\s*$/, '').trim();

const tpl = (eyebrow, h) => `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:IS;font-weight:400 900;src:url(${FONT}/instrument-sans-latin-wght-normal.woff2)}
@font-face{font-family:IS;font-weight:400 900;src:url(${FONT}/instrument-sans-latin-ext-wght-normal.woff2);unicode-range:U+0100-02BA,U+1E00-1EFF}
*{box-sizing:border-box;margin:0}
body{width:1200px;height:630px;background:#1B2B4B;color:#fff;font-family:IS,sans-serif;padding:64px 72px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.b{display:flex;align-items:center;gap:14px;font-size:34px;font-weight:800;letter-spacing:-1px}
.b i{color:#FF6B35;font-style:normal}
.mid{flex:1;display:flex;flex-direction:column;justify-content:center;gap:22px;max-width:860px}
.e{align-self:flex-start;background:rgba(255,255,255,.12);color:#FFD9C9;border-radius:999px;padding:8px 20px;font-size:24px;font-weight:700}
h1{font-weight:800;letter-spacing:-2px;line-height:1.06}
.f{font-size:24px;color:#B8C2D6;font-weight:600}
.k{position:absolute;right:-170px;top:120px;width:400px;height:400px;border-radius:50%;border:38px solid #FF6B35;opacity:.9}
.k2{position:absolute;right:6px;top:300px;width:72px;height:72px;border-radius:50%;background:#FF6B35}
</style></head><body><div class="k"></div><div class="k2"></div>
<div class="b"><svg width="50" height="50" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#fff"/><path d="M10 8v16M22 8v16M10 16h12" stroke="#1B2B4B" stroke-width="3" stroke-linecap="round"/><circle cx="16" cy="16" r="3.2" fill="#FF6B35"/></svg>Hostlio <i>Pro</i></div>
<div class="mid">${eyebrow ? `<span class="e">${esc(eyebrow)}</span>` : ''}<h1 id="h">${esc(h)}</h1></div>
<div class="f">hostliopro.com</div></body></html>`;

fs.mkdirSync(OUT, { recursive: true });
const b = await chromium.launch({ executablePath: process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
const pg = await b.newPage({ viewport: { width: 1200, height: 630 } });
// about:blank'tan file:// yazı tipine erişilemez; önce dosya kökenine geç
await pg.goto('file://' + path.join(ROOT, 'og/'));
let made = 0;
for (const p of pages) {
  if (p.key === 'home') continue;
  const h = clean(p.title);
  const eyebrow = p.type === 'article' ? BLOG[p.lang] : (p.crumb && p.crumb.toLowerCase() !== h.toLowerCase() ? p.crumb : '');
  const id = `${p.lang}-${p.key}`;
  const stamp = eyebrow + '|' + h;
  const file = path.join(OUT, id + '.jpg');
  if (stamps[id] === stamp && fs.existsSync(file)) continue;
  await pg.setContent(tpl(eyebrow, h), { waitUntil: 'load' });
  await pg.evaluate(async () => { await document.fonts.load('800 40px IS'); await document.fonts.ready; });
  if (!(await pg.evaluate(() => document.fonts.check('800 40px IS')))) throw new Error('font yüklenmedi: ' + id);
  // başlığı 3 satıra sığana kadar küçült (76px → 44px)
  await pg.evaluate(() => { const e = document.getElementById('h'); for (let s = 76; s >= 44; s -= 2) { e.style.fontSize = s + 'px'; if (e.scrollHeight <= s * 1.06 * 3 + 4) break; } });
  await pg.screenshot({ path: file, type: 'jpeg', quality: 86 });
  stamps[id] = stamp; made++;
}
await b.close();
fs.writeFileSync(stampFile, JSON.stringify(stamps, null, 0));
console.log('og images made:', made);
