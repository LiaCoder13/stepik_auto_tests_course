import pytest
from selenium.webdriver.common.by import By
import time

def test_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    btnBasket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert btnBasket, "Не найдена кнопка для добавления в корзину!"
    #time.sleep(30)