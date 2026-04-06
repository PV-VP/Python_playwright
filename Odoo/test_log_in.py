import pytest
from playwright.sync_api import expect


def test_log_in(page):
    page.goto('https://odoo-todo-dev.viyar.tech/')

    page.get_by_role("link", name="Увійти").click()
    page.get_by_role("link", name="Увійти за допомогою Keycloak").click()

    page.fill("#username", "p_mazurov@viyar.ua")
    page.fill("#password", "V2jytnbpfwsz6")
    page.get_by_role("button", name="Sign In").click()
    expect(page).to_have_url('https://odoo-todo-dev.viyar.tech/web#action=121&cids=1&menu_id=81')