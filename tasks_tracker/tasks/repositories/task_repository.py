from tasks.models.tasks_model import MyTask
from django.db import connection


class TaskRepository:
    @staticmethod
    def create_task_orm(**kwargs) -> MyTask:
        """Создание задач через ORM"""

        return MyTask.objects.create(**kwargs)
    

    @staticmethod
    def get_all_tasks_orm() -> list[MyTask]:
        """Получаем все задачи через ORM"""

        return list(MyTask.objects.all())
    

    @staticmethod
    def get_all_tasks_raw_sql() -> list[dict]:
        """Получение задач через raw SQL"""

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, title, status, is_completed, due_date
                FROM task
                ORDER BY created_at DESC
            """)
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
