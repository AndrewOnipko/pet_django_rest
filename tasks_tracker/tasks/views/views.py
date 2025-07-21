import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tasks.services.task_service import TaskService


@csrf_exempt
def task_list_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        try:
            task = TaskService.create_task(data)
            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'status': task.status,
                'is_comleted': task.is_completed,
                'due_date': str(task.due_date) if task.due_date else None,
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    elif request.method == 'GET':
        tasks = TaskService.get_all_tasks()
        result = [
            {
                'id': task.id,
                'title': task.title,
                'status': task.status,
                'is_comleted': task.is_completed,
                'due_date': str(task.due_date) if task.due_date else None,
            }
            for task in tasks
        ]
        return JsonResponse(result, safe=False)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)