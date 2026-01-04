from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.utils.html import escape

from todolist.models import Collection, Task


def index(request):
    context = {}
    collection_slug = request.GET.get('collection')
    collections = Collection.objects.order_by('slug')

    if not collection_slug:
        collection = Collection.get_default_collection()
        return redirect(f"{reverse('todolist:home')}?collection=_default")
    
    collection = get_object_or_404(Collection, slug=collection_slug)
    tasks = collection.task_set.all()

    return render(request, "todolist/index.html", context={
        "collection": collection,
        "collections": collections,
        "tasks": tasks,
        "current_user": request.user.username
    })


def get_tasks(request, collection_slug):
    collection = get_object_or_404(Collection, slug=collection_slug)
    tasks = collection.task_set.all()
    return render(request, "todolist/tasks.html", context={
        "tasks": tasks
    })
    

def add_task(request):
    collection = Collection.objects.get(slug=request.POST.get('collection'))
    task_name = escape(request.POST.get("task"))
    if task_name == "":
        return
    task = Task.objects.create(title=task_name, collection=collection)
    return render(request, 'todolist/task.html', context={
        "task": task
    })


def remove_task(request, task_pk):
    task = get_object_or_404(Task, id=task_pk)
    task.delete()
    collection = escape(request.POST.get("collection"))
    return get_tasks(request, collection)


def toggle_done(request, task_pk):
    task = get_object_or_404(Task, id=task_pk)
    task.done = not task.done
    task.save()
    return HttpResponse('')


def add_collection(request):
    collection_name = escape(request.POST.get("collection"))
    if collection_name == "":
        return
    collection, created = Collection.objects.get_or_create(name=collection_name,
                                                        slug=slugify(collection_name))
    if not created:
        return HttpResponse("This collection already exists")
    return render(request, "todolist/collection.html", context={"collection": collection})


def remove_collection(request, collection_pk):
    collection = get_object_or_404(Collection, id=collection_pk)
    collection.delete()
    return redirect('todolist:home')
