import asyncio
from playwright.async_api import async_playwright
TPL='''<html><head><style>@font-face{font-family:"Instrument Sans";font-weight:400 900;src:url(file:///home/claude/hostlio2/src/assets/fonts/instrument-sans-latin-wght-normal.woff2)}@font-face{font-family:"Instrument Sans";font-weight:400 900;src:url(file:///home/claude/hostlio2/src/assets/fonts/instrument-sans-latin-ext-wght-normal.woff2);unicode-range:U+0100-02BA}</style><style>
body{margin:0;width:1200px;height:630px;background:#1B2B4B;color:#fff;font-family:"Instrument Sans",sans-serif;display:flex;flex-direction:column;justify-content:space-between;padding:72px;box-sizing:border-box;position:relative;overflow:hidden}
.b{display:flex;align-items:center;gap:16px;font-size:40px;font-weight:800;letter-spacing:-1px}
h1{font-size:74px;line-height:1.05;letter-spacing:-2.5px;margin:0;max-width:700px;font-weight:800}
p{font-size:30px;color:#C6D2E0;margin:0}
.k{position:absolute;right:-180px;top:110px;width:420px;height:420px;border-radius:50%;border:40px solid #FF6B35;opacity:.9}
.k2{position:absolute;right:0px;top:280px;width:80px;height:80px;border-radius:50%;background:#FF6B35}
</style></head><body><div class="k"></div><div class="k2"></div>
<div class="b"><svg width="56" height="56" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#fff"/><path d="M10 8v16M22 8v16M10 16h12" stroke="#1B2B4B" stroke-width="3" stroke-linecap="round"/><circle cx="16" cy="16" r="3.2" fill="#FF6B35"/></svg>Hostlio Pro</div>
<h1>@H@</h1><p>@S@</p></body></html>'''
ICON='''<html><body style="margin:0"><svg width="%d" height="%d" viewBox="0 0 32 32"><rect width="32" height="32" rx="%s" fill="#1B2B4B"/><path d="M10 8v16M22 8v16M10 16h12" stroke="#fff" stroke-width="3" stroke-linecap="round"/><circle cx="16" cy="16" r="3.2" fill="#FF6B35"/></svg></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1200,"height":630})
        for lang,h,s in [("tr","Oteliniz uyurken Lio cevap verir.","AI destekli otel yönetim yazılımı, 30+ dil, 100+ OTA"),("en","While your hotel sleeps, Lio replies.","AI hotel management software, 30+ languages, 100+ OTAs"),
            ("es","Mientras tu hotel duerme, Lio responde.","Software de gestión hotelera con IA, 30+ idiomas, 100+ OTAs"),
            ("it","Mentre il tuo hotel dorme, Lio risponde.","Gestionale per hotel con AI, 30+ lingue, 100+ OTA"),
            ("pt","Enquanto seu hotel dorme, Lio responde.","Sistema para hotel com IA, 30+ idiomas, 100+ OTAs"),
            ("fr","Pendant que votre hôtel dort, Lio répond.","Logiciel hôtelier avec IA, 30+ langues, 100+ OTA")]:
            await pg.goto("file:///tmp/");await pg.set_content(TPL.replace("@H@",h).replace("@S@",s)); await pg.wait_for_timeout(1200)
            await pg.screenshot(path=f"/home/claude/hostlio2/src/assets/og-{lang}.png"); 
        for name,size,r in [("logo.png",512,"8"),("apple-touch-icon.png",180,"0")]:
            await pg.set_viewport_size({"width":size,"height":size}); await pg.set_content(ICON%(size,size,r))
            await pg.screenshot(path=f"/home/claude/hostlio2/src/assets/{name}",omit_background=True)
        await b.close()
asyncio.run(main())
