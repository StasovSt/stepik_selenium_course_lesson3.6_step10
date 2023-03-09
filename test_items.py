"""Запуск теста:   pytest --language=es test_items.py"""

from selenium.webdriver.common.by import By
import time

def test_add_in_basket_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Страница товара на сайте не содержит кнопку добавления в корзину"
