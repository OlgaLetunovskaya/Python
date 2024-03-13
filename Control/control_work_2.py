#**Задание 2. Автотест на калькулятор**

# Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html.
# В поле ввода по локатору `#delay` введите значение 45.
# Нажмите на кнопки:
   # - 7
   # - +
   # - 8
   # - =
# Проверьте (assert), что в окне отобразится результат `15` через 45 секунд.

import time
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

def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = ["7", "+", "8", "="]
    for button_text in buttons:
        button = browser.find_element(By.XPATH, f"//button[text()='{button_text}']")
        button.click()

    result_element = WebDriverWait(browser, 45).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )

    assert result_element.text == "15"