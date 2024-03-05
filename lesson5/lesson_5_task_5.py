#**Задание 5. Клик по кнопке с CSS-классом**

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открваем страницу http://uitestingplayground.com/classattr.
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

# Кликаем на синюю кнопку
blue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn class2 btn-primary btn-test")))
blue_button.click()

# Запускаем скрипт 3 раза подряд
for i in range(3):
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn class2 btn-primary btn-test")
    blue_button.click()
    time.sleep(1)

driver.quit()


#**Задание 5. Клик по кнопке с CSS-классом**

import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
service = FirefoxService(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

# Открваем страницу http://uitestingplayground.com/classattr.
driver.get("http://uitestingplayground.com/classattr")

# Кликаем на синюю кнопку
blue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn class2 btn-primary btn-test")))
blue_button.click()

# Запускаем скрипт 3 раза подряд
for i in range(3):
    driver = webdriver.Firefox(service = service)
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn class2 btn-primary btn-test")
    blue_button.click()
    time.sleep(1)

driver.quit()
