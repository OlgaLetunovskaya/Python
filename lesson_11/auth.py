import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login_to_trello(browser):
    browser.get("https://trello.com/")

    # Найдем поле ввода электронной почты
    email_input = browser.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_input.send_keys("leto.olga3@gmail.com")
    email_input.send_keys(Keys.RETURN)

    # Проверка, что перешли на страницу входа
    assert "login" in browser.current_url

    # Ожидание появления кнопки Google для входа
    wait = WebDriverWait(browser, 10)
    google_button = wait.until(EC.visibility_of_element_located((By.ID, "google-auth-button")))

    # Нажать кнопку Google для входа
    google_button.click()

    # Заполнить поле ввода электронной почты
    email_input = browser.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_input.send_keys("leto.olga3@gmail.com")
    email_input.send_keys(Keys.RETURN)

    # Заполнить поле ввода пароля
    password_input = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    password_input.send_keys("morozko27sobaka")
    password_input.send_keys(Keys.RETURN)

    # Проверка, что перешли на страницу входа
    assert "login" in browser.current_url
