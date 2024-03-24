#Напишите автотесты на методы приложения x-clients.
#Получить список сотрудников ДО
#Добавить нового сотрудника
#Убедится что сотрудников стало на 1 больше
#Проверить с какими данными создался новый сотрудник (Должны соответствовать тому, с какими данными его создавали)

#[GET] /employee
#[POST] /employee
#[GET] /employee/{id}
#[PATCH] /employee/{id}
#Требования:
#Тесты должны работать с библиотекой pytest.
#Тесты должны использовать библиотеку Requests.
#Тесты должны быть двух видов:
#позитивные,
#проверяющие обязательность полей.
#Логин/Пароль raphael/cool-but-crude

import pytest

def test_add_employee(employee_api):
    # Получение списка сотрудников до добавления
    old_list = employee_api.get_employees().json()
    # Данные для нового сотрудника
    new_employee = {
        "id": 22,
        "firstName": "Olga",
        "lastName": "Leto",
    }
    add_response = employee_api.add_employee(new_employee)
    assert add_response.status_code == 201
    new_employee_id = add_response.json()['id']

    # Получение списка сотрудников после добавления
    new_list = employee_api.get_employees().json()

    # Проверка увеличения количества сотрудников
    assert len(new_list) == len(old_list) + 1

    # Получение данных нового сотрудника и проверка его данных
    created_employee = employee_api.get_employee(new_employee_id).json()
    assert created_employee['firstName'] == new_employee['firstName']
    assert created_employee['lastName'] == new_employee['lastName']