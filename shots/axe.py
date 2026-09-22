import asyncio
from playwright.async_api import async_playwright
AXE=open('/tmp/package/axe.min.js').read()
PAGES=["/","/en/","/ai-misafir-asistani/","/kanal-yoneticisi/","/online-check-in/","/ozellikler/","/fiyatlandirma/","/sss/","/hakkimizda/","/iletisim/","/blog/","/blog/kucuk-otel-icin-otel-yonetim-yazilimi-secimi/","/en/pricing/","/en/contact/"]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        for path in PAGES:
            await pg.goto("http://localhost:8765"+path); await pg.add_script_tag(content=AXE); await pg.wait_for_timeout(1500)
            r=await pg.evaluate("async()=>{const r=await axe.run({runOnly:['wcag2a','wcag2aa','best-practice']});return r.violations.map(v=>v.id+' ('+v.impact+') x'+v.nodes.length+': '+v.nodes.slice(0,2).map(n=>n.target.join(' ')).join(' | '))}")
            print(path, r or "OK")
        await b.close()
asyncio.run(main())
