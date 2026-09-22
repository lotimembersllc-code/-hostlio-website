import asyncio,sys
from playwright.async_api import async_playwright
pages=sys.argv[1:]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for w,h,tag in [(1440,900,"d"),(390,844,"m")]:
            pg=await b.new_page(viewport={"width":w,"height":h})
            errs=[]; pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
            for path in pages:
                await pg.goto("http://localhost:8765"+path); await pg.wait_for_timeout(1800)
                name=path.strip("/").replace("/","_") or "home"
                await pg.screenshot(path=f"/home/claude/hostlio/shots/{name}-{tag}.png",full_page=True)
                sw=await pg.evaluate("document.documentElement.scrollWidth")
                if sw>w: print("HSCROLL",path,tag,sw)
            if errs: print("ERR",errs[:5])
        await b.close()
asyncio.run(main())
