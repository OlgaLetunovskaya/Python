import pytest
import requests

url = 'https://x-clients-be.onrender.com'
login = 'raphael'
password = 'cool-but-crude'

# Авторизация
def get_userToken():
    response = requests.post(f'{url}/auth/login', json={'username': login, 'password': password})
    return response.json()['userToken']

# Тест на метод GET /employee
def test_get_employee():
    userToken = get_userToken()
    headers = {'Authorization': f'Bearer {userToken}'}
    response = requests.get(f'{url}/employee', headers=headers)
    assert response.status_code == 200

# Тест на метод POST /employee
def test_post_employee():
    userToken = get_userToken()
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        "id": 22,
        "firstName": "Olga",
        "lastName": "Leto",
    }
    response = requests.post(f'{url}/employee', json=data, headers=headers)
    assert response.status_code == 201

    # Проверяем, что поле id присутствует в ответе
    assert 'id' in response.json()

# Тест на метод GET /employee/{id}
def test_get_employee_by_id():
    userToken = get_userToken()
    headers = {'Authorization': f'Bearer {userToken}'}
    response = requests.get(f'{url}/employee/1', headers=headers)
    assert response.status_code == 200

# Тест на метод PATCH /employee/{id}
def test_patch_employee():
    userToken = get_userToken()
    headers = {'Authorization': f'Bearer {userToken}'}
    data = {
        "id": 221,
    }
    response = requests.patch(f'{url}/employee/1', json=data, headers=headers)
    assert response.status_code == 201