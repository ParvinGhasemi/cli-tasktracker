import json
from task import Task

class TaskManager:
    def __init__(self, storage_files='tasks.json'):
        self.storage_files = storage_files
        self.tasks = []
        self.load_tasks()


    def load_tasks(self):
        try:
            with open(self.storage_files, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task_data) for task_data in tasks_data]
        except FileNotFoundError:
            self.tasks = []
            self.save_tasks()


    def save_tasks(self):
        try:
            with open(self.storage_files, 'w') as file:
                json.dump([task.to_dict() for task in self.tasks], file)
            # print("Task saved successfully.")
        except IOError as e:
            print(f'Error saving the task: {e}')


    def add_task(self, description: str):
        new_id = max((task.id for task in self.tasks), default=0) + 1
        new_task = Task(id=new_id, description=description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"{new_task.id}- {new_task.description} with status: {new_task.status} was created successfully.")


    def list_tasks(self, status=None):
        tasks_to_return = []
        for task in self.tasks:
            if status is None or task.status == status:
                print(f"{task.id}- {task.description}   -   {task.status}")


    def update_task(self, id, description: str=None, status: str=None):
        task = next((t for t in self.tasks if t.id == id), None)
        if not task:
            print('Task not found.')
        if description:
            task.update_description(description)
        if status:
            task.update_status(status)

        self.save_tasks()
        print(f'Task with ID: {id} was updated successfully.')

    def delete_task(self, task_id):
        task_found = False
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f'Task with ID: {task_id} was deleted successfully.')
                task_found = True
                break
        if not task_found:
            print('Task not found.')





