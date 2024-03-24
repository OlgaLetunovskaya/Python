import pytest
from database import get_db_session, Employee

DATABASE_URL = "postgres://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet"
@pytest.fixture(scope="function")
def db_session():
    session = get_db_session(DATABASE_URL)
    yield session
    session.rollback() 
    session.close()

def test_add_employee(employee_api, db_session):
     # Создание тестовых данных через БД
    new_test_employee = {
        "id": 22,
        "firstName": "Olga",
        "lastName": "Leto",
    }
    db_session.add(new_test_employee)
    db_session.commit()

    # Получение списка сотрудников до добавления
    old_list = employee_api.get_employees().json()

    # Данные для нового сотрудника
    new_employee = {
        "id": 23,
        "firstName": "Olga",
        "lastName": "Leto",
    }
    add_response = employee_api.add_employee(new_employee)
    assert add_response.status_code == 200
    new_employee_id = add_response.json()['id']

    # Получение списка сотрудников после добавления
    new_list = employee_api.get_employees().json()

    # Проверка увеличения количества сотрудников
    assert len(new_list) == len(old_list) + 1

    # Получение данных нового сотрудника и проверка его данных
    created_employee = employee_api.get_employee(new_employee_id).json()
    assert created_employee['name'] == new_employee['name']
    assert created_employee['position'] == new_employee['position']

    # Удаление созданных тестовых данных
    db_session.delete(new_test_employee)
    db_session.commit()
