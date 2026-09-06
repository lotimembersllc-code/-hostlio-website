#!/usr/bin/env node
// SİTE i18n KAPISI — `node scripts/i18n-check.mjs`
//
// 🔴 NEDEN (2026-09-06): site 2026-09-04'te ÖLÇÜLDÜ ve temiz çıktı
// (6 dil × 143 anahtar, eksik 0; HTML'de kullanılan 133 anahtarın hepsinin
// karşılığı var). Ama o bir KERELİK ölçümdü — kimse bir daha koşmadı ve
// koşacak bir şey de yoktu.
//
// ⛔ Sitenin arızası mobil/panelinkinden DAHA PAHALI: burası müşteri adayının
// gördüğü ilk yüzey ve bir eksik anahtar sessizce İngilizceye düşer, kimse
// hata almaz. Kardeş depolardaki kapıların site karşılığı budur.
import { readFileSync, readdirSync, statSync } from 'node:fs'
import { join } from 'node:path'

const src = readFileSync('lang.js', 'utf8')
const bas = src.indexOf('const I18N')
const son = src.indexOf('\n};', bas)
if (bas < 0 || son < 0) {
  console.error('✗ lang.js içinde I18N nesnesi bulunamadı')
  process.exit(2)
}
const I18N = new Function(`${src.slice(bas, son + 3)}; return I18N;`)()

let fail = 0
const diller = Object.keys(I18N)
const enAnahtar = Object.keys(I18N.en)
const en = new Set(enAnahtar)

// ① parite
for (const l of diller) {
  const k = new Set(Object.keys(I18N[l]))
  const eksik = enAnahtar.filter((x) => !k.has(x))
  const fazla = [...k].filter((x) => !en.has(x))
  if (eksik.length || fazla.length) {
    fail++
    console.error(`✗ ${l}: eksik ${eksik.length} ${eksik.slice(0, 8)} · fazla ${fazla.length} ${fazla.slice(0, 8)}`)
  }
}
if (!fail) console.log(`✓ parite: ${diller.length} dil × ${enAnahtar.length} anahtar, eksik 0`)

// ② boş değer
for (const l of diller) {
  const bos = Object.entries(I18N[l]).filter(([, v]) => !String(v).trim()).map(([k]) => k)
  if (bos.length) { fail++; console.error(`✗ ${l}: boş değer ${bos}`) }
}

// ③ HTML'de kullanılan her anahtarın karşılığı var mı
function walk(dir, out = []) {
  for (const e of readdirSync(dir)) {
    if (e === 'node_modules' || e.startsWith('.')) continue
    const p = join(dir, e)
    if (statSync(p).isDirectory()) walk(p, out)
    else if (e.endsWith('.html')) out.push(p)
  }
  return out
}
const eksikK = []
let toplam = 0
for (const f of walk('.')) {
  const s = readFileSync(f, 'utf8')
  for (const m of s.matchAll(/data-i18n(?:-[a-z]+)?=["']([A-Za-z0-9_]+)["']/g)) {
    toplam++
    if (!en.has(m[1])) eksikK.push(`${f} → ${m[1]}`)
  }
}
if (eksikK.length) {
  fail++
  console.error(`✗ karşılığı olmayan anahtar (${eksikK.length}):`)
  eksikK.slice(0, 20).forEach((x) => console.error(`    ${x}`))
} else {
  console.log(`✓ ${toplam} data-i18n kullanımının hepsinin karşılığı var`)
}

process.exit(fail)
