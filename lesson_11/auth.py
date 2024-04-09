import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def read_credentials():
    with open('credentials.txt', 'r') as file:
        lines = file.readlines()
        credentials = {}
        for line in lines:
            key, value = line.strip().split('=')
            credentials[key] = value
        return credentials

def test_login_to_trello(browser):
    browser.get("https://trello.com/")

    credentials = read_credentials()

    email_input = browser.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_input.send_keys(credentials['email'])
    email_input.send_keys(Keys.RETURN)

    assert "login" in browser.current_url

    wait = WebDriverWait(browser, 10)
    google_button = wait.until(EC.visibility_of_element_located((By.ID, "google-auth-button")))
    google_button.click()

    email_input = browser.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_input.send_keys(credentials['email'])
    email_input.send_keys(Keys.RETURN)

    password_input = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    password_input.send_keys(credentials['password'])
    password_input.send_keys(Keys.RETURN)

    assert "login" in browser.current_url
