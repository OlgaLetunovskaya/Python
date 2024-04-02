from selenium.webdriver.common.by import By

class InventoryPage:
    """
    Этот класс представляет собой страницу инвентаря веб-сайта.

    Методы:
    - add_item_to_cart: Добавить товар в корзину.
    - go_to_cart: Перейти на страницу корзины.
    """

    def __init__(self, driver):
        """
        Конструктор для класса InventoryPage.

        Параметры:
        - драйвер: экземпляр веб-драйвера.

        """
        self.driver = driver

    def add_item_to_cart(self, item_name: str):
        """
        Добавить товар в корзину.

        Параметры:
        - item_name (str): название добавляемого элемента.
        """

    def go_to_cart(self):
        """
        Перейти на страницу корзины.
        """