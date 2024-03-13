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
image = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img")))

# Получите значение атрибута `src` у 3-й картинки.
third_image_src = driver.find_elements(By.TAG_NAME, "img")[2].get_attribute("src")

# Выведите значение в консоль.
print(third_image_src)


driver.quit()
