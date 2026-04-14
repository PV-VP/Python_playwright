import os
import random
import string
import pytest

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

def test_log_in(page: Page, open_odoo):
    random_name = "Meeting " + "".join(random.choices(string.ascii_letters, k=6))   # рандомні данні для назви зустрічі
    random_fill = "".join(random.choices(string.ascii_letters, k=80))               # рандомні данні для опису зустрічі

    expect(page).to_have_url("https://odoo-todo-dev.viyar.tech/web")    # очікуваний перехід на сторінку

    page.get_by_title("Календар").click()
    page.get_by_role("button", name="Новий").click()               # створюєм зутріч
    page.get_by_placeholder("напр. Бізнес ланч").fill(random_name)      # назва зустрічі(заповнюється "Meeting " + random_name)
    page.locator("#description_0").click()                              # знаходим поле Опис
    page.locator("#description_0").type(random_fill)                    # заповнюємо ранодомними данними
    page.locator("#categ_ids_0").click()                                # відкриваємо дропдаун міток
    expect(page.get_by_text("київ")).to_be_visible()                    # перевіряємо що опція "київ" є у списку
    page.get_by_role("option", name="київ").click()                # вибираємо мітку "київ"
    page.locator("#categ_ids_0").blur()                                 # знімаємо фокус щоб форма зрозуміла що вибір зроблено
    page.locator("i.fa-cloud-upload").click()                           # зберігаємо зустріч
