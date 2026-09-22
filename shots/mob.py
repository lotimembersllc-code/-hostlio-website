import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for w,name in [(360,'m360'),(390,'m390'),(768,'m768')]:
            m=await b.new_page(viewport={"width":w,"height":900}); await m.emulate_media(reduced_motion="reduce")
            await m.goto("http://localhost:8767"+(sys.argv[1] if len(sys.argv)>1 else "/")); await m.wait_for_timeout(900)
            await m.screenshot(path=f"shots/{name}.png")
            print(name, await m.evaluate("document.documentElement.scrollWidth"))
        await b.close()
asyncio.run(main())
