#** Задание 1. Автотест на заполнение формы **

#Напишите автотест(запускается через `pytest`).
# Откройте страницу: https: // bonigarcia.dev / selenium - webdriver - java / data - types.html.
# Заполните форму значениями:
#| First name | Иван |
#| Last name | Петров |
#| Address | Ленина, 55 - 3 |
#| Email | test @ skypro.com |
#| Phone number | +7985899998787 |
#| Zip code |*оставить пустым |
#| City | Москва |
#| Country | Россия |
#| Job position | QA |
#| Company | SkyPro |
# Нажмите кнопку Submit.
# Проверьте( assert), что поле `Zip code ` подсвечено красным.
# Проверьте( assert), что остальные поля подсвечены зеленым.

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

def test_form_validation(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "First name": "Иван",
        "Last name": "Петров",
        "Address": "Ленина, 55 - 3",
        "Email": "test@skypro.com",
        "Phone number": "+7985899998787",
        "Zip code": "",
        "City": "Москва",
        "Country": "Россия",
        "Job position": "QA",
        "Company": "SkyPro"
    }

    for field, value in form_data.items():
        input_field = browser.find_element(By.NAME, field)
        input_field.send_keys(value)

    submit_button = browser.find_element(By.ID, "submit")
    submit_button.click()

    zip_code_field = browser.find_element(By.NAME, "Zip code")
    assert "rgb(255, 0, 0)" in zip_code_field.value_of_css_property("border-color")

    for field in form_data.keys():
        input_field = browser.find_element(By.NAME, field)
        assert "rgb(0, 128, 0)" in input_field.value_of_css_property("border-color")