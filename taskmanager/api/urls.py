
from django.urls import path
from .views import TaskListCreateView, TasksRetrieveUpdateDestroyView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name = "task-list-create"),
    path("tasks/<int:pk>/", TasksRetrieveUpdateDestroyView.as_view(), name= "task-retrieve-update-destroy")  

]