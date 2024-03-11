from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

# Перейти на страницу http://uitestingplayground.com/textinput
driver.implicitly_wait(15)

driver.get("http://uitestingplayground.com/textinput")

# Поиск поля ввода на веб-странице
input_field = driver.find_element(By.CSS_SELECTOR,"#newButtonName")

# Очищение поля ввода
input_field.clear()

# Указать в поле ввода текст SkyPro.
input_field.send_keys("SkyPro")

# Нажать на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

# Получить текст кнопки и вывод в консоль
button_text = blue_button.text
print(button_text)

driver.quit()