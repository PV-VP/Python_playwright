from playwright.sync_api import Page, expect

def test_create_task(page, open_odoo):

    page.get_by_title("Створити Задачу/Заявку").click()



