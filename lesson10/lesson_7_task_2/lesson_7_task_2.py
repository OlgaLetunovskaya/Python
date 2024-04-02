import pytest
import time
import allure
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Calculator Test")
@allure.title("Тест функциональности калькулятора с задержкой")
def test_calculator(browser):
    page = CalculatorPage(browser)

    with allure.step("Открыть страницу калькулятора"):
        page.open_page()

    with allure.step("Установить значение задержки равным 45"):
        page.set_delay("45")

    with allure.step("Выполнить расчет: 7 + 8"):
        page.click_button("7")
        time.sleep(1)
        page.click_button("8")
        time.sleep(1)
        page.click_button("=")

    with allure.step("Проверить результат через 45 секунд"):
        result = page.get_result()
        assert result == "15"

    page.close_page()