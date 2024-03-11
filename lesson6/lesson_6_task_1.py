#**Задание 1. Нажатие на кнопку**

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Перейти на страницу http://uitestingplayground.com/ajax.
driver.implicitly_wait(25)
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку.
blue_bt_click=driver.find_element(By.CSS_SELECTOR,"#ajaxButton").click()

# Получить текст из зеленой плашки.
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Вывести его в консоль *(”Data loaded with AJAX get request.”).
print(txt)

driver.quit()