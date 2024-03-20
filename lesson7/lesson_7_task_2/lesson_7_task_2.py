# **Задание 2. Автотест на калькулятор**

# Напишите автотест (запускается через `pytest`).

# Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html.
# В поле ввода по локатору `#delay` введите значение 45.
# Нажмите на кнопки:
   # - 7
   # - +
   # - 8
   # - =
# Проверьте (assert), что в окне отобразится результат `15` через 45 секунд.

import pytest
from CalculatorPage import CalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(page):
    page = CalculatorPage(driver)

    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    page.set_delay("45")
    page.click_button("7")
    time.sleep(1)
    page.click_button("8")
    time.sleep(1)
    page.click_button("=")
    result = page.get_result()
    assert result == "15"



