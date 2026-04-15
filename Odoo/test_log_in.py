import os

from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

def test_log_in(page, open_odoo):
    page.get_by_role("link", name="Увійти").click()
    page.get_by_role("link", name="Увійти за допомогою Keycloak").click()
    page.locator("#username").fill(os.environ["TEST_USER"])
    page.locator("#password").fill(os.environ["TEST_PASS"])
    page.get_by_role("button", name="Sign In").click()

