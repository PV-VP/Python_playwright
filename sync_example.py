from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import browser

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  #headless=False - что бы страница открылась
    page = browser.new_page()
    page.goto('https://viyar.ua/ua/')
    page.screenshot(path='screenshot/homepage.png')
    browser.close()



    #https://www.youtube.com/watch?v=Y7p6a5HowLU