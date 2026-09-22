import asyncio, pathlib
from playwright.async_api import async_playwright
AXE=open('/tmp/axe/package/axe.min.js').read()
D=pathlib.Path("dist")
PAGES=["/","/en/","/fr/","/pt/"]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        for path in PAGES:
            await pg.goto("http://localhost:8767"+path); await pg.add_script_tag(content=AXE); await pg.wait_for_timeout(1600)
            r=await pg.evaluate("async()=>{const r=await axe.run({runOnly:['wcag2a','wcag2aa','best-practice']});return r.violations.map(v=>v.id+' ('+v.impact+') x'+v.nodes.length+': '+v.nodes.slice(0,2).map(n=>n.target.join(' ')).join(' | '))}")
            if r: print(path, r)
            w=await pg.evaluate("document.documentElement.scrollWidth")
        # mobile overflow
        for w in (360,390):
            m=await b.new_page(viewport={"width":w,"height":900})
            for path in PAGES:
                await m.goto("http://localhost:8767"+path)
                sw=await m.evaluate("document.documentElement.scrollWidth")
                if sw>w: print("overflow",w,path,sw)
        await b.close(); print("done", len(PAGES))
asyncio.run(main())
