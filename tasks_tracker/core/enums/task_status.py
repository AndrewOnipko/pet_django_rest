from django.db.models import TextChoices


class TaskStatus(TextChoices):
    PENDING = "pending", "Ожидает"
    IN_PROGRESS = "in_progress", "В процессе"
    DONE = "completed", "Завершено"
    CANCELED = "canceled", "Отменено"

    @classmethod
    def choices(cls):
        return [(key.value, key.label) for key in cls]