#**Задание 3. Дождаться картинки**

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

# Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождитесь загрузки всех картинок.
image = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container")))

# Получите значение атрибута `src` у 3-й картинки.
src = driver.find_element(By.CSS_SELECTOR, "#image-container").get_attribute('#award')

# Выведите значение в консоль.
print(src)