from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        self.driver.get('https://www.saucedemo.com/inventory.html')
        self.driver.find_element(By.ID, 'user-name').send_keys('standart_user').click()
        self.driver.find_element(By.ID, 'password').send_keys('secret_sause').click()
        self.driver.find_element(By.ID, 'login-button').click()
