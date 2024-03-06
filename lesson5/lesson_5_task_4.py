#**Задание 4. Клик по кнопке без ID**


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем страницу http://uitestingplayground.com/dynamicid
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

# Кликаем на синюю кнопку
blue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
blue_button.click()

# Запускаем скрипт 3 раза подряд
for i in range(3):
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
    time.sleep(2)

driver.quit()

#**Задание 4. Клик по кнопке без ID**

import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
service = FirefoxService(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)
driver.maximize_window()

# Открываем страницу http://uitestingplayground.com/dynamicid
driver.get("http://uitestingplayground.com/dynamicid")

# Кликаем на синюю кнопку
blue_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
blue_button.click()

# Запускаем скрипт 3 раза подряд
for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
    time.sleep(2)
driver.quit()
