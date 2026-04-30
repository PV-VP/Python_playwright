
from playwright.sync_api import Page, expect
from helpers import generate_random_name, generate_random_fill_20_symbols

def test_create_task(page:Page, open_odoo):


    page.get_by_title("Створити Задачу/Заявку").click()                         #клікаєм Створити Задачу/Заявку
    page.get_by_role("button", name="Нова").click()                             #створюєм натиска.чи кнопку Нова
    page.get_by_text("Пошук...").click()                                        #віжкриваєм список підрозділів
    page.get_by_text("Казначейство", exact=True).click()                        #жмем Казначейство
    page.get_by_text("Пошук...").blur()                                         #убираєм фокус з пошуку
    page.locator("button.creation_form_tabs_item", has_text="Заявки на кошти").click() #Вибір Групи Шаблонів(форма заявки)
    page.get_by_text("Заявка на кошти готівкою", exact=True).click()      #вибераэм готівку
    page.get_by_placeholder("Вкажіть іншу особу, якщо виконавець не є співробітником компанії").fill(generate_random_name())
    page.get_by_placeholder("Вкажіть призначення платежу").fill(generate_random_fill_20_symbols())
    page.get_by_text("Оберіть філію, до якої буде віднесено вашу витрату").click()
    page.get_by_text("Без філії", exact=True).click()


    page.screenshot(path="../screenshot/task.png") #робим скрін

