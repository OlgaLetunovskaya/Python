#**Задание 6. Модальное окно**

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открваем страницу http://the-internet.herokuapp.com/entry_ad.
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")

# В модальном окне нажимаем на кнопку `Сlose`.
modal_close_button = (WebDriverWait(driver, 30).until
    (EC.presence_of_element_located((By.CLASS_NAME, "modal-footer"))))
close_button = modal_close_button.find_element(By.TAG_NAME, "p")

time.sleep(1)
close_button.click()

time.sleep(1)

driver.quit()


#**Задание 6. Модальное окно**

import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
service = FirefoxService(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)

# Открваем страницу http://the-internet.herokuapp.com/entry_ad.

driver.get("http://the-internet.herokuapp.com/entry_ad")

# В модальном окне нажимаем на кнопку `Сlose`.
modal_close_button = (WebDriverWait(driver, 30).until
    (EC.presence_of_element_located((By.CLASS_NAME, "modal-footer"))))
close_button = modal_close_button.find_element(By.TAG_NAME, "p")

time.sleep(1)
close_button.click()

time.sleep(1)

driver.quit()
