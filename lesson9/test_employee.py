import pytest
from database import engine
from database import Session
from faker import Faker
from sqlalchemy.orm import close_all_sessions
from database import get_db_session, add_employee, delete_employee, Employee

faker = Faker()

@pytest.fixture(scope="function")

def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()
@pytest.fixture(scope="function")
def fake_employee_data():
    return {
        "id": faker.random_int(min=1, max=9999),
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
    }

def test_add_and_delete_employee(db_session, fake_employee_data):
    # Добавление нового сотрудника
    add_employee(db_session, fake_employee_data)

    # Получение и проверка данных нового сотрудника
    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data.first_name == fake_employee_data['firstName']
    assert employee_data.last_name == fake_employee_data['lastName']

    # Удаление созданного сотрудника после теста
    delete_employee(db_session, fake_employee_data['id'])

    # Проверка, что сотрудник удалён
    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data is None
    
def test_update_employee(db_session, fake_employee_data):
    # Добавление нового сотрудника
    add_employee(db_session, fake_employee_data)

    # Получение и проверка данных нового сотрудника
    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data.first_name == fake_employee_data['firstName']
    assert employee_data.last_name == fake_employee_data['lastName']

    # Новые данные для обновления сотрудника
    new_employee_data = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
    }

    # Обновление данных сотрудника
    update_employee(db_session, fake_employee_data['id'], new_employee_data)

    # Получение и проверка обновленных данных сотрудника
    updated_employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert updated_employee_data.first_name == new_employee_data['firstName']
    assert updated_employee_data.last_name == new_employee_data['lastName']

    # Удаление созданного сотрудника после теста
    delete_employee(db_session, fake_employee_data['id'])

    # Проверка, что сотрудник удален
    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data is None
