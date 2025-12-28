from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.utils.html import escape

from todolist.models import Collection, Task


# Create your views here.
def index(request):
    context = {}
    collection_slug = request.GET.get('collection')
    if not collection_slug:
        collection = Collection.get_default_collection()
        # return redirect(f"{reverse('todolist:home')}?collection=_default")
    else:
        collection = get_object_or_404(Collection, slug=collection_slug)
    context = get_context(collection)
    return render(request, "todolist/index.html", context=context)


def get_tasks(request, collection_slug):
    context = {}
    collection = get_object_or_404(Collection, slug=collection_slug)
    context = get_context(collection)
    return render(request, "todolist/index.html", context=context)
    

def add_task(request, collection_pk):
    context = {}
    task_name = escape(request.POST.get("task"))
    collection = get_object_or_404(Collection, id=collection_pk)
    task, _ = Task.objects.create(title=task_name)
    context = get_context(collection)


def add_collection(request):
    collection_name = request.POST.get("collection")
    collection, created = Collection.objects.get_or_create(name=collection_name,
                                                        slug=slugify(collection_name))
    if not created:
        return HttpResponse("This collection already exists")
    return redirect('todolist:home')


def remove_collection(request, collection_pk):
    collection = get_object_or_404(Collection, id=collection_pk)
    collection.delete()
    return redirect('todolist:home')


# TOOLS
def get_context(collection):
    context = {}
    context['current_collection'] = collection
    context['tasks'] = collection.task_set.all()
    context['collections'] = Collection.objects.order_by('slug')
    return context
