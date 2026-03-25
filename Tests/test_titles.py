from xml.etree.ElementPath import xpath_tokenizer

from playwright.sync_api import Page, expect


def test_main_page_title(page: Page):
    page.goto('https://viyar.ua/ua')
    assert page.title() == 'ВіЯр - інтернет-магазин меблевої фурнітури, аксесуарів і матеріалів для виготовлення меблів в Україні'

def test_catalogue(page: Page):
    page.goto('https://viyar.ua/ua')
    page.locator('xpath=/html/body/div[2]/div/main/div/section/div/div[2]/div[1]/div/div/div/div/div[1]/button/span[2]').click()
    expect(page).to_have_title('Плитні матеріали Viyar.ua | Купити у Києві, Україні')



    #https://www.youtube.com/watch?v=I5Hdc1rDYkk
    #https://www.youtube.com/watch?v=IH0W5bm4orc - git