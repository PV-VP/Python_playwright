from shutil import which

from playwright.async_api import async_playwright
import asyncio

from sync_example import browser


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://viyar.ua/ua/catalog/')
        await page.screenshot(path ='../screenshot/catalogue.png')
        await browser.close()
asyncio.run(main())