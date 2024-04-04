import pytest
import allure
from LoginPage import LoginPage
from InventoryPage import InventoryPage
from CartPage import CartPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Тест корзины покупок")
@allure.title("Тестирование функциональности корзины покупок")
def test(browser):
    login_page = LoginPage(browser)
    login_page.open()

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(browser)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Оформление заказа"):
        cart_page = CartPage(browser)
        cart_page.checkout()

    with allure.step("Заполнение данных формы"):
        cart_page.fill_out_form("John", "Doe", "12345")

    with allure.step("Проверка общей стоимости"):
        total_price = cart_page.get_total_price()
        assert total_price == "$58"
