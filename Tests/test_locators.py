from playwright.sync_api import Page, expect

def test_locator_role(page: Page):
    page.goto('https://viyar.ua/ua/')
    page.get_by_role("button", name='Меблева фурнітура').click()
    expect(page).to_have_title('Меблева фурнітура | Viyar.ua | Купити у Києві, Україні')
    page.get_by_role("button", name='Змінити мову').click()
    expect(page.get_by_text('Polski')).to_be_visible()


    #https://www.youtube.com/watch?v=zSrRTk4IkFY