"""Site kapısı: python3 scripts/check.py  (build sonrası; CI ve Vercel buildCommand çalıştırır)

FAIL sayılanlar:
  - kırık iç bağlantı (href) ve eksik asset (src, srcset, poster, data-webm/mp4, imagesrcset)
  - geçersiz JSON-LD / JSON veri blokları
  - karşılıklı olmayan hreflang, yerel sayfada h1 yok / birden fazla
  - indekslenen sayfalarda tekrarlanan <title> veya description; uzun title (>65) / description (>160)
  - satır içi betik ya da on*= özniteliği (CSP script-src 'self' bunları engeller — O4)
  - doldurulmamış fiyat yer tutucusu (⟦…⟧, pricing.py)
  - vercel.json yönlendirme hedefi ya da sitemap adresi dist'te yok
İsteğe bağlı: --live-prices → pricing.py değerlerini canlı `plans` ucuyla karşılaştırır (ağ gerekir).
"""
import re, json, pathlib, collections, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "dist"
pages = {}
for f in D.rglob("*.html"):
    rel = "/" + str(f.relative_to(D))
    u = rel[:-10] if rel.endswith("index.html") else rel
    pages[u] = f.read_text()


def exists(p):
    p = p.split("?")[0].split("#")[0]
    return p in pages or (D / p.lstrip("/")).exists() or (D / (p.lstrip("/") + ".html")).exists()


bad = collections.Counter(); titles = collections.defaultdict(list); descs = collections.defaultdict(list); issues = []
for u, h in pages.items():
    for a in re.findall(r'href="(/[^"#?]*)', h):
        if not exists(a): bad[(u, a)] += 1
    for a in re.findall(r'(?:src|poster|data-webm|data-mp4)="(/[^"]+)"', h):
        if not exists(a): issues.append(("asset", u, a))
    for ss in re.findall(r'(?:srcset|imagesrcset)="([^"]+)"', h):
        for part in ss.split(","):
            a = part.strip().split(" ")[0]
            if a.startswith("/") and not exists(a): issues.append(("srcset", u, a))
    for m in re.findall(r'<script type="application/(?:ld\+)?json"[^>]*>(.*?)</script>', h, re.S):
        try: json.loads(m)
        except Exception as e: issues.append(("json", u, str(e)))
    # O4: CSP gate — executable inline scripts and inline event handlers are not allowed
    for tag, body in re.findall(r'<script(\s[^>]*)?>(.*?)</script>', h, re.S):
        tag = tag or ""
        if "src=" not in tag and "application/ld+json" not in tag and "application/json" not in tag:
            issues.append(("inline-script", u, body[:60]))
    for m in re.findall(r'<[a-z][^>]*\son[a-z]+="[^"]*"', h):
        issues.append(("inline-handler", u, m[:80]))
    if "⟦" in h: issues.append(("price-token", u, h[h.index("⟦"):h.index("⟦") + 30]))
    noindex = 'name="robots" content="noindex' in h
    t = re.search(r"<title>(.*?)</title>", h)
    d = re.search(r'<meta name="description" content="(.*?)"', h)
    if not noindex:
        if t: titles[t.group(1)].append(u)
        if d: descs[d.group(1)].append(u)
        import html as _h
        if t and len(_h.unescape(t.group(1))) > 65: issues.append(("title-len", u, len(_h.unescape(t.group(1)))))
        if d and len(_h.unescape(d.group(1))) > 160: issues.append(("desc-len", u, len(_h.unescape(d.group(1)))))
    # hreflang reciprocity
    if u.endswith("404.html"): continue
    alts = dict(re.findall(r'<link rel="alternate" hreflang="([\w-]+)" href="https://hostliopro.com([^"]+)"', h))
    for l, p in alts.items():
        if p not in pages: issues.append(("hreflang-missing", u, p)); continue
        back = dict(re.findall(r'<link rel="alternate" hreflang="([\w-]+)" href="https://hostliopro.com([^"]+)"', pages[p]))
        if u not in back.values() and l != "x-default": issues.append(("hreflang-nonrecip", u, p))
    if u.startswith(("/es/", "/it/", "/pt/", "/fr/")):
        if "<h1" not in h: issues.append(("noh1", u))
        if h.count("<h1") > 1: issues.append(("multih1", u))

# text outputs must not carry price tokens either
for f in ["llms.txt", "llms-full.txt", "sitemap.xml"]:
    if "⟦" in (D / f).read_text(): issues.append(("price-token", f))

# sitemap URLs exist
for loc in re.findall(r"<loc>https://hostliopro.com([^<]+)</loc>", (D / "sitemap.xml").read_text()):
    if loc not in pages: issues.append(("sitemap-missing", loc))

# vercel.json: every redirect destination resolves (path part, without query)
vc = json.loads((ROOT / "vercel.json").read_text())
for r in vc.get("redirects", []):
    dst = r["destination"].split("?")[0]
    if dst.startswith("/") and not exists(dst): issues.append(("redirect-dest", r["source"], dst))
srcs = collections.Counter((r["source"], json.dumps(r.get("has"))) for r in vc.get("redirects", []))
issues += [("redirect-dup", s) for s, n in srcs.items() if n > 1]

dup_t = [(t, v) for t, v in titles.items() if len(v) > 1]
dup_d = [(t[:40], v) for t, v in descs.items() if len(v) > 1]
print("pages", len(pages)); print("broken", list(bad)[:20])
print("dup titles", dup_t[:10])
print("dup descs", dup_d[:10])
print("issues", issues[:30], len(issues))

if "--live-prices" in sys.argv:
    sys.path.insert(0, str(ROOT))
    import urllib.request, pricing, build
    req = urllib.request.Request(build.PLANS_ENDPOINT, headers={"Authorization": "Bearer " + build.PLANS_ANON})
    live = json.load(urllib.request.urlopen(req, timeout=15))
    diff = []
    if live.get("early_bird") != pricing.EARLY_BIRD: diff.append(("early_bird", pricing.EARLY_BIRD, live.get("early_bird")))
    for p in live.get("plans", []):
        if p["id"] not in pricing.BY_ID: continue
        if p["monthly"]["amount"] != pricing.monthly(p["id"]): diff.append((p["id"], "monthly", pricing.monthly(p["id"]), p["monthly"]["amount"]))
        if p["annual"]["amount"] != pricing.annual(p["id"]): diff.append((p["id"], "annual", pricing.annual(p["id"]), p["annual"]["amount"]))
    print("live prices", "OK" if not diff else diff)
    if diff: issues.append(("live-prices", diff))

fail = bool(bad) or bool(issues) or bool(dup_t) or bool(dup_d)
print("RESULT:", "FAIL" if fail else "OK")
sys.exit(1 if fail else 0)
