from rest_framework import serializers
from tasks_tracker.tasks.models.tasks_model import MyTask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTask
        fields = ['id', 'title', 'description', 'status', 'due_date', 'is_completed']