from django.urls import path
from first_app.views import add_task,show_task,edit_task,delete_task

urlpatterns = [
    path('add_task/',add_task,name="addTask"),
    path('show_task/',show_task,name="showtask"),
    path('edit_task/<int:id>',edit_task,name="edit_task"),
    path('delete_task/<int:id>',delete_task,name="delete_task"),
]
