from django.urls import path
from .views import TaskListView, TasksCreateView, TasksDeleteView, TasksDetailView, TasksUpdateView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks-list'),
    path('tasks/create/', TasksCreateView.as_view(), name='tasks-create'),
    path('tasks/<int:pk>/', TasksDetailView.as_view(), name='tasks-detail'),
    path('tasks/update/<int:pk>/', TasksUpdateView.as_view(), name='tasks-update'),
    path('tasks/delete/<int:pk>/', TasksDeleteView.as_view(), name='tasks-delete'),

]