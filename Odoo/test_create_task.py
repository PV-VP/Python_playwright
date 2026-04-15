import random
import string
from playwright.sync_api import Page, expect
from helpers import generate_task_name

def test_create_task(page, open_odoo):
    random_name = "Task " + "".join(random.choices(string.ascii_letters, k=6))

    page.get_by_title("Створити Задачу/Заявку").click()
    page.get_by_role("button", name="Нова").click()
    page.get_by_text("Пошук...").click()
    expect(page.get_by_text("Казначейство")).to_be_visible()
    page.locator(".selection_item", has_text="Казначейство").click()
    page.get_by_text("Пошук...").blur()
    page.locator("button.creation_form_tabs_item", has_text="Загальні").click()
    page.get_by_placeholder("Вкажіть назву задачі").fill(generate_task_name()) #не знаходить
    #print(page.locator("input.text_widget_input").count())