import pytest
from database import engine
from database import Session
from faker import Faker
from database import add_employee, delete_employee, update_employee, Employee

faker = Faker()

@pytest.fixture(scope="function")
def db_session() -> Session:
    """
    Фикстура для создания сессии базы данных.

    Возвращается:
    - Session: Сессия базы данных.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def fake_employee_data() -> dict:
    """
    Генерация фейковых данных для сотрудника.

    Возвращается:
    - dict: Словарь с данными сотрудника.
    """
    return {
        "id": faker.random_int(min=1, max=9999),
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
    }

def test_add_and_delete_employee(db_session, fake_employee_data):
    """
    Тест на добавление и удаление сотрудника.

    Параметры:
    - db_session (Session): Сессия базы данных.
    - fake_employee_data (dict): Данные для добавления сотрудника.
    """
    add_employee(db_session, fake_employee_data)

    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data.first_name == fake_employee_data['firstName']
    assert employee_data.last_name == fake_employee_data['lastName']

    delete_employee(db_session, fake_employee_data['id'])
    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data is None

def test_update_employee(db_session, fake_employee_data):
    """
    Тест на обновление данных сотрудника.

    Параметры:
    - db_session (Session): Сессия базы данных.
    - fake_employee_data (dict): Данные сотрудника.
    """
    add_employee(db_session, fake_employee_data)

    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data.first_name == fake_employee_data['firstName']
    assert employee_data.last_name == fake_employee_data['lastName']

    new_employee_data = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
    }

    update_employee(db_session, fake_employee_data['id'], new_employee_data)

    updated_employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert updated_employee_data.first_name == new_employee_data['firstName']
    assert updated_employee_data.last_name == new_employee_data['lastName']

    delete_employee(db_session, fake_employee_data['id'])
    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data is None
