import os
import random
import string

from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()


def test_log_in(page):
    random_name = "Meeting " + "".join(random.choices(string.ascii_letters, k=6))   # рандомні данні для назви зустрічі
    random_fill = "".join(random.choices(string.ascii_letters, k=80))               # рандомні данні для опису зустрічі

    page.goto(os.environ["APP_URL"])
    page.get_by_role("link", name="Увійти").click()
    page.get_by_role("link", name="Увійти за допомогою Keycloak").click()
    page.locator("#username").fill(os.environ["TEST_USER"])
    page.locator("#password").fill(os.environ["TEST_PASS"])
    page.get_by_role("button", name="Sign In").click()                  # authorization
    expect(page).to_have_url("https://odoo-todo-dev.viyar.tech/web")    # очікуваний перехід на сторінку
    page.get_by_title("Головне меню").click()
    page.get_by_title("Календар").click()
    page.get_by_role("button", name="Новий").click()                    # створюєм зутріч
    page.get_by_placeholder("напр. Бізнес ланч").fill(random_name)      # назва зустрічі(заповнюється "Meeting " + random_name)
    page.locator("#description_0").click()                              # знаходим поле Опис
    page.locator("#description_0").type(random_fill)                    # заповнюємо ранодомними данними
    page.locator("#categ_ids_0").click()                                # відкриваємо дропдаун міток
    expect(page.get_by_text("київ")).to_be_visible()                    # перевіряємо що опція "київ" є у списку
    page.get_by_role("option", name="київ").click()                     # вибираємо мітку "київ"
    page.locator("#categ_ids_0").blur()                                 # знімаємо фокус щоб форма зрозуміла що вибір зроблено
    page.locator("i.fa-cloud-upload").click()                           # зберігаємо зустріч
