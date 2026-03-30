from playwright.sync_api import Page, expect

def test_locator_role(page: Page): #тест вияр базар(находим поле, нажимаем, проверяем выпадающий список)
    page.goto('https://viyar.ua/ua/')
    page.get_by_role("link", name="Знайти мебляра").click()




def test_locator_placeholder(page: Page):
    page.goto('https://viyar.ua/ua/')
    page.get_by_placeholder('Я шукаю...').fill('17990')
    page.keyboard.press('Enter')
    expect(page.get_by_text('Інформація про наявність товарів на філії Гавела, 23 може бути неточною. Уточнюйте, будь ласка, наявність у менеджерів чи у контакт-центрі.')).to_be_visible()



    #https://www.youtube.com/watch?v=zSrRTk4IkFY