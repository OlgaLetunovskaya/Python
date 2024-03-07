#**Задание 8. Форма авторизации**

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Откройте страницу http://the-internet.herokuapp.com/login.
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

#В поле username введите значение `tomsmith`.
username_field = driver.find_element(By.ID,"username")
username_field.send_keys("tomsmith")

#В поле password введите значение `SuperSecretPassword!`.
password_field = driver.find_element(By.ID,"password")
password_field.send_keys("SuperSecretPassword!")

#Нажмите кнопку `Login`.
login_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
login_button.click()

time.sleep(5)

driver.quit()


#**Задание 8. Форма авторизации**

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
service = FirefoxService(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

#Откройте страницу http://the-internet.herokuapp.com/login.
driver.get("http://the-internet.herokuapp.com/login")

#В поле username введите значение `tomsmith`.
username_field = driver.find_element(By.ID,"username")
username_field.send_keys("tomsmith")

#В поле password введите значение `SuperSecretPassword!`.
password_field = driver.find_element(By.ID,"password")
password_field.send_keys("SuperSecretPassword!")

#Нажмите кнопку `Login`.
login_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
login_button.click()

time.sleep(5)

driver.quit()


