import pytest


def test_add_todo(page) -> None:
    page.goto("https://viyar.ua/ua/")
    page.locator(".header-catalog__select").click()
    page.get_by_role("banner").get_by_role("button", name="Плитні матеріали").click()
    page.get_by_role("button", name="Добре").click()



