
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.showTodos,name='todolist'),
    path('update_task/<str:id>/',views.updateTask, name="update_task"),
    path('delete_task/<str:id>/',views.deleteTask,name="delete_task")
]
