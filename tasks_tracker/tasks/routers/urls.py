from django.urls import path
from .. import views
from ..views.views_drf import TaskAPIView

urlpatterns = [
    # path('tasks/', views.task_list_create),
    path('tasks/', TaskAPIView.as_view()),
    path('tasks/<int:pk>/', TaskAPIView.as_view()),
]