from tasks.repositories.task_repository import TaskRepository
from core.enums.task_status import TaskStatus
from django.shortcuts import get_object_or_404
from ..models.tasks_model import MyTask 

class TaskService:
    @staticmethod
    def create_task(data: dict):
        """Бизнес логика создания задачи. TODO - валидация, логгирование, интеграции и т.д."""

        task_data = {
            "title": data.get("title"),
            "description": data.get("description", ""),
            "status": data.get("status", TaskStatus.PENDING),
            "due_date": data.get("due_date"),
            "is_completed": data.get("is_completed", False),
        }

        return TaskRepository.create_task_orm(**task_data)
    

    @staticmethod
    def get_all_tasks():
        """Возвращает все задачи через ORM"""

        return TaskRepository.get_all_tasks_orm()
    

    @staticmethod
    def get_all_tasks_raw():
        """Возвращает все задачи через сырой SQL"""

        return TaskRepository.get_all_tasks_raw_sql()
    

    @staticmethod
    def update_task(pk: int, data: dict):
        """Обновляет задачу (завершает или отменяет)"""

        task = get_object_or_404(MyTask, pk=pk)
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return task