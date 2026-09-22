import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); m=await b.new_page(viewport={"width":360,"height":900})
        for path in sys.argv[1:]:
            await m.goto("http://localhost:8767"+path)
            r=await m.evaluate("""()=>[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>361&&e.children.length<9).slice(0,4).map(e=>e.tagName+'.'+e.className+' '+Math.round(e.getBoundingClientRect().right)+' '+(e.textContent||'').slice(0,60))""")
            print(path, r)
        await b.close()
asyncio.run(main())
