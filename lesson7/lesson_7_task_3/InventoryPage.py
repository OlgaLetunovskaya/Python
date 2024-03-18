from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        self.driver.find_element_by_xpath(f"//div[text()='{item_name}']/following-sibling::button").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
