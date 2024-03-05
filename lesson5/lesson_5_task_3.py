#**Задание 3. Клик по кнопке**

from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

#Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#Пять раз кликните на кнопку `Add Element`.
for i in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR,"button[onclick='addElement()']")
    add_button.click()

#Соберите со страницы список кнопок `Delete`.
delete_buttons = driver.find_elements(By.CSS_SELECTOR,"button[onclick='deleteElement()']")

#Выведите на экран размер списка.
print("Размер списка кнопок Delete:", len(delete_buttons))


sleep(1)


#**Задание 3. Клик по кнопке**

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
service = FirefoxService(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)
from time import sleep

#Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

#Пять раз кликните на кнопку `Add Element`.
for i in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR,"button[onclick='addElement()']")
    add_button.click()

#Соберите со страницы список кнопок `Delete`.
delete_buttons = driver.find_elements(By.CSS_SELECTOR,"button[onclick='deleteElement()']")

#Выведите на экран размер списка.
print("Размер списка кнопок Delete:", len(delete_buttons))


sleep(1)
