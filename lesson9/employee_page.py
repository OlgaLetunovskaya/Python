import requests

class EmployeePage:
    BASE_URL = "https://x-clients-be.onrender.com/employee"

    def __init__(self, token):
        self.headers = {'Authorization': f'Bearer {token}'}

    def get_employees(self):
        return requests.get(self.BASE_URL, headers=self.headers)

    def add_employee(self, employee_data):
        return requests.post(self.BASE_URL, json=employee_data, headers=self.headers)

    def get_employee(self, employee_id):
        return requests.get(f"{self.BASE_URL}/{employee_id}", headers=self.headers)

    def update_employee(self, employee_id, employee_data):
        return requests.patch(f"{self.BASE_URL}/{employee_id}", json=employee_data, headers=self.headers)
