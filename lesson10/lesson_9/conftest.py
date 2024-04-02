import pytest
import requests
import psycopg2
from sqlalchemy.orm import Session
from database import engine


@pytest.fixture(scope="session")
def auth_token() -> str:
    """
    Фикстура для получения токена авторизации.

    Returns:
    - str: Токен авторизации.
    """
    login_url = "https://x-clients-be.onrender.com/auth/login"
    credentials = {"login": "raphael", "password": "cool-but-crude"}
    response = requests.post(login_url, json=credentials)
    assert response.status_code == 200
    return response.json()["access_token"]


@pytest.fixture
def employee_api(auth_token) -> EmployeePage:
    """
    Фикстура для взаимодействия с API сотрудников.

    Parameters:
    - auth_token (str): Токен авторизации.

    Returns:
    - EmployeePage: Объект EmployeePage.
    """
    from pages.employee_page import EmployeePage
    return EmployeePage(auth_token)


@pytest.fixture(scope="function")
def db_session() -> Session:
    """
    Фикстура для создания сессии базы данных.

    Returns:
    - Session: Сессия базы данных.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()