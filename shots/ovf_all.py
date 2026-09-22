import asyncio, pathlib
from playwright.async_api import async_playwright
D=pathlib.Path("dist")
PAGES=sorted("/"+str(f.parent.relative_to(D))+"/" if str(f.parent.relative_to(D))!="." else "/" for f in D.rglob("index.html"))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for w in (360,390,768):
            m=await b.new_page(viewport={"width":w,"height":900})
            for path in PAGES:
                await m.goto("http://localhost:8767"+path.replace("//","/"))
                sw=await m.evaluate("document.documentElement.scrollWidth")
                if sw>w: print("overflow",w,path,sw)
        await b.close(); print("done",len(PAGES))
asyncio.run(main())
