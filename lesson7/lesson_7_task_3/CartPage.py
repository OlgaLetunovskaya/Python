from selenium.webdriver.common.keys import Keys

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element_by_css_selector("[data-test='shopping-cart']")

    def fill_out_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, 'first-name').send_keys(first_name).click()
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name).click()
        self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code).click()
        self.driver.find_element(By.ID, 'continue').click()

        self.driver.find_element(By.CLASS_NAME, "cart_button").click()

    def get_total_price(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text

    def quit(self):
        self.driver.quit()
