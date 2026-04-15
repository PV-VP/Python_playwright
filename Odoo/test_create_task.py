import random
import string
from playwright.sync_api import Page, expect
from helpers import generate_task_name, generate_fibonacci

def test_create_task(page, open_odoo):


    page.get_by_title("Створити Задачу/Заявку").click()                         #клікаєм Створити Задачу/Заявку
    page.get_by_role("button", name="Нова").click()                             #створюєм натиска.чи кнопку Нова
    page.get_by_text("Пошук...").click()                                        #віжкриваєм список підрозділів
    expect(page.get_by_text("Казначейство")).to_be_visible()                    #очікуєм що буде Казначейство
    page.locator(".selection_item", has_text="Казначейство").click()            #жмем Казначейство
    page.get_by_text("Пошук...").blur()                                         #убираєм фокус з пошуку
    page.locator("button.creation_form_tabs_item", has_text="Загальні").click() #Вибір Групи Шаблонів(форма заявки)
    page.get_by_placeholder("Вкажіть назву задачі").fill(generate_task_name())  #заповнюєм назву довільно
    page.locator("span.vsd_placeholder", has_text="Виберіть значення").click()  #вибрати приорітет задачі
    page.locator(".selection_item", has_text="Низький").click()                 #натиснути на пріоритет
    page.get_by_placeholder("0").first.fill(generate_fibonacci())                              #


    page.screenshot(path="../screenshot/task.png") #робим скрін