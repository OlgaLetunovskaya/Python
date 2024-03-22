#Напишите класс, который предоставляет удобные методы для работы с задачами в
# сервисе [https://sky-todo-list.herokuapp.com](https://sky-todo-list.herokuapp.com/):

#- Создание.
#- Переименование.
#- Удаление.
#- Получение списка.
#- Получение конкретной задачи из списка.
#- Отметка задачи «Выполнена».
#- Снятие отметки «Выполнена».

class SkyTodoList:

def__init__(self):
    self.base_url = "https://sky-todo-list.herokuapp.com"

def create_task(self, task_name):
    url = f"{self.base_url}/tasks"
    data = {"name": task_name}
    response = requests.post(url, json=data)
    return response.json()

def rename_task(self, task_id, new_name):
    url = f"{self.base_url}/tasks/{task_id}/rename"
    data = {"name": new_name}
    response = requests.put(url, json=data)
    return response.json()

def delete_task(self, task_id):
    url = f"{self.base_url}/tasks/{task_id}"
    response = requests.delete(url)
    return response.json()

def get_tasks_list(self):
    url = f"{self.base_url}/tasks"
    response = requests.get(url)
    return response.json()

def get_task(self, task_id):
    url = f"{self.base_url}/tasks/{task_id}"
    response = requests.get(url)
    return response.json()

def mark_task_completed(self, task_id):
    url = f"{self.base_url}/tasks/{task_id}/complete"
    response = requests.put(url)
    return response.json()

def mark_task_incomplete(self, task_id):
    url = f"{self.base_url}/tasks/{task_id}/incomplete"
    response = requests.put(url)
    return response.json()
