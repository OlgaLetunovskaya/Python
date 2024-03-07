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
blue_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
blue_button.click()

# Запускаем скрипт 3 раза подряд
for i in range(3):
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
    time.sleep(1)

driver.quit()



#**Задание 5. Клик по кнопке с CSS-классом**

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.maximize_window()

# Открваем страницу http://uitestingplayground.com/classattr.

driver.get("http://uitestingplayground.com/classattr")

# Кликаем на синюю кнопку
blue_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
blue_button.click()

# Запускаем скрипт 3 раза подряд
for i in range(3):
    driver = webdriver.Firefox()
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()
    time.sleep(1)

driver.quit()
