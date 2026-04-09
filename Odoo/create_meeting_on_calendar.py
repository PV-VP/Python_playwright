import os
import random
import string

from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()
random_name = "Meeting " + "".join(random.choices(string.ascii_letters, k=6))

def test_log_in(page):
    page.goto(os.environ["APP_URL"])
    page.get_by_role("link", name="Увійти").click()
    page.get_by_role("link", name="Увійти за допомогою Keycloak").click()
    page.locator("#username").fill(os.environ["TEST_USER"])
    page.locator("#password").fill(os.environ["TEST_PASS"])
    page.get_by_role("button", name="Sign In").click()
    expect(page).to_have_url("https://odoo-todo-dev.viyar.tech/web")
    page.get_by_title("Головне меню").click()
    page.get_by_title("Календар").click()
    page.get_by_role("button", name="Новий").click()
    page.get_by_placeholder("напр. Бізнес ланч").fill(random_name)
    page.locator("i.fa-cloud-upload").click()
