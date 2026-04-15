import os
import pytest
from playwright.sync_api import Page, expect

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

@pytest.fixture     # логін
def open_odoo(page: Page):                  #фікстура, тобто прекондішн. Кажем шо спочатку треба перейти на сайт, а в функції нижче передаеєм як параметр. Якщо додати аутоюз=тру, то буде запускатись при кожному тесту, можно в параметр не передавати
    page.goto(os.environ["APP_URL"])
    page.get_by_role("link", name="Увійти").click()
    page.get_by_role("link", name="Увійти за допомогою Keycloak").click()
    page.locator("#username").fill(os.environ["TEST_USER"])
    page.locator("#password").fill(os.environ["TEST_PASS"])
    page.get_by_role("button", name="Sign In").click()
    page.get_by_title("Головне меню").click()
