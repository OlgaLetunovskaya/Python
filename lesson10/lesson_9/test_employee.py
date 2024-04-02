import pytest
from faker import Faker
from database import engine, Session, add_employee, delete_employee, Employee

faker = Faker()

@pytest.fixture(scope="function")
def db_session():
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

@pytest.fixture(scope="function")
def fake_employee_data():
    """
    Фикстура для генерации фейковых данных о сотруднике.

    Returns:
    - dict: Словарь с данными о сотруднике.
    """
    return {
        "id": faker.random_int(min=1, max=9999),
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
    }

def test_add_and_update_employee(db_session, fake_employee_data):
    """
    Тест на добавление и обновление данных сотрудника в базе.

    Parameters:
    - db_session: Сессия базы данных.
    - fake_employee_data: Фейковые данные о сотруднике.
    """
    add_employee(db_session, fake_employee_data)

    # Получение и проверка данных о новом сотруднике
    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data.first_name == fake_employee_data['firstName']
    assert employee_data.last_name == fake_employee_data['lastName']

    # Обновление данных сотрудника
    updated_employee_data = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
    }
    db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).update(updated_employee_data)
    db_session.commit()

    # Получение и проверка обновленных данных сотрудника
    updated_employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert updated_employee_data.first_name == updated_employee_data['firstName']
    assert updated_employee_data.last_name == updated_employee_data['lastName']

    # Удаление созданного сотрудника после теста
    delete_employee(db_session, fake_employee_data['id'])

    # Проверка удаления сотрудника
    employee_data = db_session.query(Employee).filter(Employee.id == fake_employee_data['id']).first()
    assert employee_data is None