from django.contrib import admin
from todolist.models import Collection, Task


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'done', 'collection')


admin.site.register(Collection)
admin.site.register(Task)