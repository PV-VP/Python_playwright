
from playwright.sync_api import Page, expect
from helpers import generate_task_name, generate_fibonacci

def test_create_task(page, open_odoo):


    page.get_by_title("Створити Задачу/Заявку").click()                         #клікаєм Створити Задачу/Заявку
    page.get_by_role("button", name="Нова").click()                             #створюєм натиска.чи кнопку Нова
    page.get_by_text("Пошук...").click()                                        #віжкриваєм список підрозділів
    page.get_by_text("Казначейство", exact=True).click()                #жмем Казначейство
    page.get_by_text("Пошук...").blur()                                         #убираєм фокус з пошуку
    page.locator("button.creation_form_tabs_item", has_text="Загальні").click() #Вибір Групи Шаблонів(форма заявки)
    page.get_by_placeholder("Вкажіть назву задачі").fill(generate_task_name())  #заповнюєм назву довільно
    page.locator("span.vsd_placeholder", has_text="Виберіть значення").click()  #вибрати приорітет задачі
    page.locator(".selection_item", has_text="Низький").click()                 #натиснути на пріоритет
    page.get_by_placeholder("0").first.fill(generate_fibonacci())               # Story point (план) - заповнює числами фібоначі(рандом)
    page.locator("#crnd_widget_vr_start_date input").fill("08.08.2015")
    page.locator("#crnd_widget_deadline_date input").fill("08.08.2026")
    page.locator(".note-editable").click()
    page.keyboard.type('321')
    page.get_by_role("button", name="Поставити задачу").click()
    page.screenshot(path="../screenshot/task.png") #робим скрін

    #поки не працює, буде перероблюватись логіка