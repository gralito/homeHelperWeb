from django.urls import path
from todolist import views


app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='home'),
    path('get-tasks/<int:collection_pk>', views.get_tasks, name='get-tasks'),
    path('add-collection', views.add_collection, name='add-collection'),
    path('remove-collection/<int:collection_pk>', views.remove_collection, name='remove-collection'),
]