import pytest
import allure
from selenium import webdriver
from pages.DataFormPage import DataFormPage
from pages.ValidationPage import ValidationPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Тест на заполнение формы")
@allure.title("Отправка и валидация тестовой формы")
def test_fill_data_form(browser):
    data_page = DataFormPage(browser)
    validation_page = ValidationPage(browser)

    with allure.step("Откройте страницу формы данных"):
        data_page.open()

    with allure.step("Заполните форму"):
        data_page.enter_first_name("Иван")
        data_page.enter_last_name("Петров")
        # Add steps for filling out the remaining fields

    with allure.step("Отправьте форму"):
        data_page.submit_form()

    with allure.step("Проверка выделения почтового индекса"):
        assert validation_page.is_zip_code_red()

    with allure.step("Проверка выделения других полей"):
        assert validation_page.are_other_fields_green()