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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def login():
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.find_element(By.ID,'user-name').send_keys('standart_user').click()
    driver.find_element(By.ID, 'password').send_keys('secret_sause').click()
    driver.find_element(By.ID, 'login-button').click()

def test_add_to_card():
    login()

    driver.find_element_by_css_selector("[data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element_by_css_selector("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element_by_css_selector("[data-test='add-to-cart-sauce-labs-onesie']").click()

    time.sleep(2)
    cart_button = driver.find_element_by_css_selector("[data-test='shopping-cart']")
    cart_button.click()

    checkout_button = driver.find_element_by_css_selector("[data-test='checkout']")
    checkout_button.click()

    driver.find_element(By.ID, 'first-name').send_keys('John').click()
    driver.find_element(By.ID, 'last-name').send_keys('Doe').click()
    driver.find_element(By.ID, 'postal-code').send_keys('12345').click()
    driver.find_element(By.ID, 'continue').click()

    time.sleep(2)

    total = driver.find_element(By.CLASS_NAME,'.summary_info_label').text
    assert total == '$58.29'

    driver.quit()
