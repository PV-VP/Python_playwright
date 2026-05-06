
from playwright.sync_api import Page, expect
from helpers import generate_random_name, generate_random_fill_20_symbols, generate_random_digit

def test_create_task(page:Page, open_odoo):

    page.get_by_title("Створити Задачу/Заявку").click()   #клікаєм Створити Задачу/Заявку
    page.get_by_role("button", name="Нова").click()  #створюєм натиска.чи кнопку Нова
    page.get_by_text("Пошук...").click()   #віжкриваєм список підрозділів
    page.get_by_text("Казначейство", exact=True).click() #жмем Казначейство
    page.get_by_text("Пошук...").blur()  #убираєм фокус з пошуку
    page.locator("button.creation_form_tabs_item", has_text="Заявки на кошти").click()  #Вибір Групи Шаблонів(форма заявки)
    page.get_by_text("Заявка на кошти готівкою", exact=True).click()   #вибераэм готівку
    page.get_by_placeholder("Вкажіть іншу особу, якщо виконавець не є співробітником компанії").fill(generate_random_name())
    page.get_by_placeholder("Вкажіть призначення платежу").fill(generate_random_fill_20_symbols())
    page.locator("#crnd_widget_vr_name_affiliate_id").click()  #Філія підрозділу
    page.locator("#crnd_widget_vr_name_affiliate_id").get_by_text("Новокостянтинівська", exact=True).click()
    page.locator("#crnd_widget_vr_cash_withdrawal_affiliate_id").click() #Філія видачі коштів *
    page.locator("#crnd_widget_vr_cash_withdrawal_affiliate_id").get_by_text("Новокостянтинівська", exact=True).click()
    page.get_by_placeholder("Вкажіть суму оплати").fill(generate_random_digit())  #заповнюєм сумму оплати
    page.get_by_placeholder("Вкажіть суму оплати").blur()
    page.get_by_text("Оберіть валюту оплати").click()
    page.get_by_text("USD", exact=True).click()
    page.locator("#crnd_widget_vr_name_functional_cost_unit_id").click() #Підрозділ витрати
    page.locator("#crnd_widget_vr_name_functional_cost_unit_id").get_by_text("Адміністрація Новокостянтинівська", exact=True).click()
    page.get_by_placeholder("Пошук проєкту витрат...").fill(generate_random_fill_20_symbols())


    page.screenshot(path="../screenshot/task.png") #робим скрін