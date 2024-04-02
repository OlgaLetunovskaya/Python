import requests
import allure

class EmployeePage:
    """
    Класс для взаимодействия с API сотрудников.

    Атрибуты:
    - BASE_URL (str): Базовый URL для запросов к API.
    - headers (dict): Заголовки запроса с токеном авторизации.
    """

    BASE_URL = "https://x-clients-be.onrender.com/employee"

    def __init__(self, token: str):
        """
        Инициализация объекта класса EmployeePage.

        Параметры:
        - token (str): Токен авторизации.
        """
        self.headers = {'Authorization': f'Bearer {token}'}

    @allure.step("GET Employees")
    def get_employees(self) -> requests.Response:
        """
        Получение списка сотрудников.

        Возвращается:
        - requests.Response: Ответ от сервера.
        """
        response = requests.get(self.BASE_URL, headers=self.headers)
        assert response.status_code == 200
        return response

    @allure.step("POST Employee")
    def add_employee(self, employee_data: dict) -> requests.Response:
        """
        Добавление нового сотрудника.

        Параметры:
        - employee_data (dict): Данные о сотруднике.

        Возвращается:
        - requests.Response: Ответ от сервера.
        """
        return requests.post(self.BASE_URL, json=employee_data, headers=self.headers)

    @allure.step("GET Employee")
    def get_employee(self, employee_id: int) -> requests.Response:
        """
        Получение данных конкретного сотрудника.

        Параметры:
        - employee_id (int): ID сотрудника.

        Возвращается:
        - requests.Response: Ответ от сервера.
        """
        return requests.get(f"{self.BASE_URL}/{employee_id}", headers=self.headers)

    @allure.step("PATCH Employee")
    def update_employee(self, employee_id: int, employee_data: dict) -> requests.Response:
        """
        Обновление данных сотрудника.

        Параметры:
        - employee_id (int): ID сотрудника.
        - employee_data (dict): Новые данные о сотруднике.

        Возвращается:
        - requests.Response: Ответ от сервера.
        """
        return requests.patch(f"{self.BASE_URL}/{employee_id}", json=employee_data, headers=self.headers)