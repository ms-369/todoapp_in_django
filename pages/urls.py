from django.contrib import admin
from django.urls import path, include
from .views import add_task, delete_task, done_task

urlpatterns = [
    path("",add_task ),
    path("delete_task/<int:task_id>/",delete_task, name="delete_task"),
    path("done_task/<int:task_id>/",done_task, name="done_task"),
]