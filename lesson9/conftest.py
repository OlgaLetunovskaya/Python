import pytest
import requests
from sqlalchemy.orm import Session
from database import engine

@pytest.fixture(scope="session")
def auth_token():
    #Фикстура для получения токена авторизации.
    login_url = "https://x-clients-be.onrender.com/auth/login"
    credentials = {"login": "raphael", "password": "cool-but-crude"}
    response = requests.post(login_url, json=credentials)
    assert response.status_code == 200
    return response.json()["access_token"]

@pytest.fixture
def employee_api(auth_token):
    #Фикстура для взаимодействия с API сотрудников.
    from pages.employee_page import EmployeePage
    return EmployeePage(auth_token)

@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()