
    """lesson_7_task_1"""
import pytest
import allure
from selenium import webdriver
from DataFormPage import DataFormPage
from ValidationPage import ValidationPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_data_form(browser):
    data_page = DataFormPage(browser)
    validation_page = ValidationPage(browser)
    data_page.open()

    with allure.step("Заполнение формы с данными"):
        data_page.enter_first_name("Иван")
        data_page.enter_last_name("Петров")
        data_page.enter_address("Ленина, 55-3")
        data_page.enter_email("test@skypro.com")
        data_page.enter_phone_number("+7985899998787")
        data_page.enter_zip_code("")
        data_page.enter_city("Москва")
        data_page.enter_country("Россия")
        data_page.enter_job_position("QA")
        data_page.enter_company("SkyPro")

    with allure.step("Заполнение формы"):
        data_page.submit_form()

    with allure.step("Проверка, выделено ли поле с почтовым индексом красным цветом"):
        assert validation_page.is_zip_code_red()

    with allure.step("Проверка, выделены ли другие поля зеленым цветом"):
        assert validation_page.are_other_fields_green()

@allure.title("Отправка формы тестовых данных")
@allure.description("Заполнение формы с данными и проверка правильности")
@allure.feature("Функция формирования данных")
@allure.severity(allure.severity_level.NORMAL)
def test_fill_data_form_with_allure(browser):
    data_page = DataFormPage(browser)
    validation_page = ValidationPage(browser)
    data_page.open()

    with allure.step("Заполнение формы с данными"):
        data_page.enter_first_name("Иван")
        data_page.enter_last_name("Петров")
        data_page.enter_address("Ленина, 55-3")
        data_page.enter_email("test@skypro.com")
        data_page.enter_phone_number("+7985899998787")
        data_page.enter_zip_code("")
        data_page.enter_city("Москва")
        data_page.enter_country("Россия")
        data_page.enter_job_position("QA")
        data_page.enter_company("SkyPro")

    with allure.step("Отправка формы"):
        data_page.submit_form()

    with allure.step("Проверка, выделено ли поле с почтовым индексом красным цветом"):
        assert validation_page.is_zip_code_red()

    with allure.step("Проверка, выделены ли другие поля зеленым цветом"):
        assert validation_page.are_other_fields_green()

    """lesson_7_task_2"""
import pytest
import allure
import time
from CalculatorPage import CalculatorPage
from selenium import webdriver



@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(page):
    page = CalculatorPage(browser)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    page.set_delay("45")
    page.click_button("7")
    time.sleep(1)
    page.click_button("8")
    time.sleep(1)
    page.click_button("=")
    result = page.get_result()
    assert result == "15"


@allure.title("Функциональность тестового калькулятора")
@allure.description("Тестирование основных операций с калькулятором")
@allure.feature("Функции калькулятора")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator_with_allure(page):
    page = CalculatorPage(browser)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    page.set_delay("45")

    with allure.step("Выполнение расчета: 7 + 8"):
        page.click_button("7")
        time.sleep(1)
        page.click_button("8")
        time.sleep(1)
        page.click_button("=")

    with allure.step("Проверка результата"):
        result = page.get_result()
        assert result == "15"

    """lesson_7_task_3"""
import pytest
import allure
from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shopping_flow(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart("Рюкзак Sauce Labs")
    inventory_page.add_item_to_cart("Футболка Sauce Labs Bolt")
    inventory_page.add_item_to_cart("Комбинезончик от Sauce Labs")

    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    with allure.step("Заполнение формы оформления заказа"):
        cart_page.fill_out_form("John", "Doe", "12345")

    with allure.step("Получение общей цены и проверка"):
        total_price = cart_page.get_total_price()
        assert total_price == "$58.29"

    cart_page.quit()


@allure.title("Тестирование покупок")
@allure.description("Тестирование процесса совершения покупок от входа в систему до оформления заказа")
@allure.feature("Совершение покупки")
@allure.severity(allure.severity_level.NORMAL)
def test_shopping_flow_with_allure(driver):
    login_page = LoginPage(driver)
    login_page.open()

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart("Рюкзак Sauce Labs")
    inventory_page.add_item_to_cart("Футболка Sauce Labs Bolt")
    inventory_page.add_item_to_cart("Комбинезончик от Sauce Labs")

    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    with allure.step("Заполнение формы оформления заказа"):
        cart_page.fill_out_form("John", "Doe", "12345")

    with allure.step("Получение общей цены и проверка"):
        total_price = cart_page.get_total_price()
        assert total_price == "$58.29"

    cart_page.quit()

    """lesson9"""
import pytest
import allure
from faker import Faker
from database import get_db_connection, add_employee, delete_employee
faker = Faker()
@pytest.fixture(scope="function")
def db_connection():
    """
    Фикстура, обеспечивающая подключение к базе данных для теста.
    """
    connection = get_db_connection()
    yield connection
    connection.close()
@pytest.fixture(scope="function")
def fake_employee_data():
    """
    Фикстура, генерирующая поддельные данные о сотрудниках для тестирования.
 Возвращается:
 dict: Словарь, содержащий поддельные данные о сотрудниках.
    """
    return {
        "id": faker.random_int(min=1, max=9999),
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
    }
@allure.title("Добавление сотрудника")
@allure.description("Добавление нового сотрудника в базу данных")
@allure.feature("Управление персоналом")
def test_add_employee(employee_api, db_connection, fake_employee_data):
    """
    Тестирование добавления нового сотрудника в базу данных и проверка данных.
 Аргументы:
 employee_api (объект): Объект для взаимодействия с API сотрудника.
 db_connection (объект): Объект подключения к базе данных.
 fake_employee_data (dict): Словарь, содержащий поддельные данные о сотрудниках.
    """
    with allure.step("Добавление нового сотрудника"):
        add_employee(db_connection, fake_employee_data)
    with allure.step("Извлечение и проверка новых данных о сотрудниках"):
        employee_data = employee_api.get_employee(fake_employee_data['id']).json()
        assert employee_data['firstName'] == fake_employee_data['firstName']
        assert employee_data['lastName'] == fake_employee_data['lastName']
    with allure.step("Удаление созданного сотрудника после тестирования"):
        delete_employee(db_connection, fake_employee_data['id'])
