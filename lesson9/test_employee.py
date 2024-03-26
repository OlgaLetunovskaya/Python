import pytest
from faker import Faker
from database import get_db_connection, add_employee, delete_employee

faker = Faker()

@pytest.fixture(scope="function")
def db_connection():
    connection = get_db_connection()
    yield connection
    connection.close()

@pytest.fixture(scope="function")
def fake_employee_data():
    return {
        "id": faker.random_int(min=1, max=9999),
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
    }

def test_add_employee(employee_api, db_connection, fake_employee_data):
    # Добавление нового сотрудника
    add_employee(db_connection, fake_employee_data)

    # Получение и проверка данных нового сотрудника
    employee_data = employee_api.get_employee(fake_employee_data['id']).json()
    assert employee_data['firstName'] == fake_employee_data['firstName']
    assert employee_data['lastName'] == fake_employee_data['lastName']

    # Удаление созданного сотрудника после теста
    delete_employee(db_connection, fake_employee_data['id'])
