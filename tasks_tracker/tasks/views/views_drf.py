from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.services.task_service import TaskService
from tasks.serializers import TaskSerializer

class TaskAPIView(APIView):
    def get(self, request):
        tasks = TaskService.get_all_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = TaskService.create_task(serializer.validated_data)
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk=None):
        updated = TaskService.update_task(pk, request.data)
        return Response(TaskSerializer(updated).data)