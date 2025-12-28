from django.urls import path
from todolist import views


app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='home'),
    path('get-tasks/<str:collection_slug>', views.get_tasks, name='get-tasks'),
    path('add-task', views.add_task, name='add-task'),
    path('add-collection', views.add_collection, name='add-collection'),
    path('remove-collection/<int:collection_pk>', views.remove_collection, name='remove-collection'),
]