import requests

class EmployeePage:
    BASE_URL = "https://x-clients-be.onrender.com/employee"

    def __init__(self, token):
        self.headers = {'Authorization': f'Bearer {token}'}
    #GET
    def get_employees(self):
        return requests.get(self.BASE_URL, headers=self.headers)
        assert response.status_code == 200

    #POST
    def add_employee(self, employee_data):
        return requests.post(self.BASE_URL, json=employee_data, headers=self.headers)

    #GET
    def get_employee(self, employee_id):
        return requests.get(f"{self.BASE_URL}/{employee_id}", headers=self.headers)

    #PATCH
    def update_employee(self, employee_id, employee_data):
        return requests.patch(f"{self.BASE_URL}/{employee_id}", json=employee_data, headers=self.headers)


