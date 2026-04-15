import os
import pytest
from helpers import generate_random_name, generate_random_fill
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

def test_log_in(page: Page, open_odoo):

    page.get_by_title("Календар").click()
    page.get_by_role("button", name="Новий").click()               # створюєм зутріч
    page.get_by_placeholder("напр. Бізнес ланч").fill(generate_random_name())      # назва зустрічі(заповнюється "Meeting " + random_name)
    page.locator("#description_0").click()                              # знаходим поле Опис
    page.locator("#description_0").type(generate_random_fill())                    # заповнюємо ранодомними данними
    page.locator("#categ_ids_0").click()                                # відкриваємо дропдаун міток
    expect(page.get_by_text("київ")).to_be_visible()                    # перевіряємо що опція "київ" є у списку
    page.get_by_role("option", name="київ").click()                # вибираємо мітку "київ"
    page.locator("#categ_ids_0").blur()                                 # знімаємо фокус щоб форма зрозуміла що вибір зроблено
    page.locator("i.fa-cloud-upload").click()                           # зберігаємо зустріч
