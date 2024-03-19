from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, ):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(value)

    def click_button(self, button_text):
        self.driver.find_element_by_xpath(f"//button[contains(text(), '{button_text}')]").click()

    def get_result(self):
        return self.driver.find_element(By.ID, "result").text

    def close_page(self):
        self.driver.quit()
