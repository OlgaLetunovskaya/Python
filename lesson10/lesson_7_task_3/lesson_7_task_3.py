import pytest
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
import allure

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

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()

    cart_page.fill_out_form("John", "Doe", "12345")

    total_price = cart_page.get_total_price()
    assert total_price == "$58.