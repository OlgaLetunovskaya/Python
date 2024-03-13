#**Задание 3. Автотест на интернет-магазин**

# Откройте сайт магазина: https://www.saucedemo.com/.
# Авторизуйтесь как пользователь `standard_user`.
# Добавьте в корзину товары:
    #- Sauce Labs Backpack
    #- Sauce Labs Bolt T-Shirt
    #- Sauce Labs Onesie
# Перейдите в корзину.
# Нажмите Checkout.
# Заполните форму своими данными:
    #- имя,
    #- фамилия,
    #- почтовый индекс.
# Нажмите кнопку Continue.
# Прочитайте со страницы итоговую стоимость ( `Total` ).
# Закройте браузер.
# Проверьте, что итоговая сумма равна **$58.29.**

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping_cart(browser):
    browser.get("https://www.saucedemo.com/")


    username_input = browser.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()


    products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for product in products:
        add_to_cart_button = browser.find_element(By.XPATH, f"//div[text()='{product}']/following-sibling::div/button")
        add_to_cart_button.click()


    cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()


    checkout_button = browser.find_element(By.XPATH, "//a[text()='CHECKOUT']")
    checkout_button.click()


    first_name_input = browser.find_element(By.ID, "first-name")
    first_name_input.send_keys("John")
    last_name_input = browser.find_element(By.ID, "last-name")
    last_name_input.send_keys("Doe")
    postal_code_input = browser.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("12345")


    continue_button = browser.find_element(By.XPATH, "//input[@type='submit']")
    continue_button.click()


    total_amount = browser.find_element(By.CLASS_NAME, "summary_total_label").text

    assert total_amount == "$58.29"