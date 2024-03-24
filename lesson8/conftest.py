import pytest
import requests

@pytest.fixture(scope="session")
def auth_token():
    """Фикстура для получения токена авторизации."""
    login_url = "https://x-clients-be.onrender.com/auth/login"
    credentials = {"login": "raphael", "password": "cool-but-crude"}
    response = requests.post(login_url, json=credentials)
    assert response.status_code == 200
    return response.json()["access_token"]

@pytest.fixture
def employee_api(auth_token):
    """Фикстура для взаимодействия с API сотрудников."""
    from pages.employee_page import EmployeePage
    return EmployeePage(auth_token)