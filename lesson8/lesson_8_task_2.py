import requests

class SkyTodoList:
    def __init__(self):
        self.base_url = 'https://sky-todo-list.herokuapp.com'

    def create_task(self, title):
        response = requests.post(f'{self.base_url}/tasks', json={'title': title})
        return response.json()

    def rename_task(self, task_id, new_title):
        response = requests.put(f'{self.base_url}/tasks/{task_id}', json={'title': new_title})
        return response.json()

    def delete_task(self, task_id):
        response = requests.delete(f'{self.base_url}/tasks/{task_id}')
        return response.ok

    def get_tasks(self):
        response = requests.get(f'{self.base_url}/tasks')
        return response.json()

    def get_task(self, task_id):
        response = requests.get(f'{self.base_url}/tasks/{task_id}')
        return response.json()

    def mark_task_as_completed(self, task_id):
        response = requests.put(f'{self.base_url}/tasks/{task_id}/completed')
        return response.ok

    def mark_task_as_not_completed(self, task_id):
        response = requests.delete(f'{self.base_url}/tasks/{task_id}/completed')
        return response.ok

# Пример использования
todo_list = SkyTodoList()

# Создание задачи
new_task = todo_list.create_task('Buy groceries')
print(new_task)

# Переименование задачи
renamed_task = todo_list.rename_task(new_task['id'], 'Buy fruits')
print(renamed_task)

# Получение списка задач
tasks = todo_list.get_tasks()
print(tasks)

# Отметка задачи как выполненной
completed = todo_list.mark_task_as_completed(new_task['id'])
print(completed)

# Получение конкретной задачи
task = todo_list.get_task(new_task['id'])
print(task)