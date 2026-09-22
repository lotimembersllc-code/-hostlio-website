import re, json, pathlib, collections
D = pathlib.Path(__file__).resolve().parent.parent / "dist"
pages = {}
for f in D.rglob("*.html"):
    rel = "/" + str(f.relative_to(D))
    u = rel[:-10] if rel.endswith("index.html") else rel
    pages[u] = f.read_text()
exists = lambda p: p in pages or (D / p.lstrip("/")).exists() or (D/(p.lstrip("/")+".html")).exists()
bad=collections.Counter(); titles=collections.defaultdict(list); descs=collections.defaultdict(list); issues=[]
for u, h in pages.items():
    for a in re.findall(r'href="(/[^"#?]*)', h):
        if not exists(a): bad[(u,a)]+=1
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(m)
        except Exception as e: issues.append(("jsonld",u,str(e)))
    t = re.search(r"<title>(.*?)</title>", h); 
    if t: titles[t.group(1)].append(u)
    d = re.search(r'<meta name="description" content="(.*?)"', h)
    if d: descs[d.group(1)].append(u)
    # hreflang reciprocity
    if u.endswith("404.html"): continue
    alts = dict(re.findall(r'<link rel="alternate" hreflang="([\w-]+)" href="https://hostliopro.com([^"]+)"', h))
    for l, p in alts.items():
        if p not in pages: issues.append(("hreflang-missing", u, p)); continue
        back = dict(re.findall(r'<link rel="alternate" hreflang="([\w-]+)" href="https://hostliopro.com([^"]+)"', pages[p]))
        if u not in back.values(): issues.append(("hreflang-nonrecip", u, p))
    if u.startswith(("/es/","/it/","/pt/","/fr/")):
        n=len(re.findall(r'hreflang="[\w-]+"', h))
        if "<h1" not in h: issues.append(("noh1",u))
        if h.count("<h1")>1: issues.append(("multih1",u))
print("pages", len(pages)); print("broken", list(bad)[:20])
print("dup titles", [(t,v) for t,v in titles.items() if len(v)>1][:10])
print("dup descs", [(t[:40],v) for t,v in descs.items() if len(v)>1][:10])
print("issues", issues[:20], len(issues))
import sys
fail = bool(bad) or bool(issues) or any(len(v)>1 for v in titles.values())
print("RESULT:", "FAIL" if fail else "OK")
for u in sorted(pages):
    if False:
        t=re.search(r"<title>(.*?)</title>", pages[u]).group(1); d=re.search(r'<meta name="description" content="(.*?)"', pages[u]).group(1)
        if len(t)>70 or len(d)>170 or len(d)<110: print("len", u, len(t), len(d))

sys.exit(1 if fail else 0)
