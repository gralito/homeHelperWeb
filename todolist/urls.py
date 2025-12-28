from django.urls import path
from todolist import views


app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='todolist-main')
]