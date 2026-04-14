from playwright.sync_api import Page, expect

def test_create_task(page, open_odoo):

    page.get_by_title("Створити Задачу/Заявку").click()
    page.get_by_role("button", name="Нова").click()
    page.get_by_text("Пошук...").click()
    expect(page.get_by_text("Казначейство")).to_be_visible()
    page.locator(".selection_item", has_text="Казначейство").click()
    page.get_by_text("Пошук...").blur()
    page.locator("button.creation_form_tabs_item", has_text="Загальні")
    page.get_by_placeholder("Вкажіть назву задачі").fill('asd') #не знаходить
    #print(page.locator("input.text_widget_input").count())