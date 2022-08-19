from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list),
    path('login', views.login),
    path('register', views.register),
    path('todo/<int:id>', views.edit_todo),
    path('todo/done/<int:id>', views.done_todo)
]