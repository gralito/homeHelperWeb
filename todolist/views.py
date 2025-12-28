from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.utils.text import slugify

from todolist.models import Collection

# Create your views here.
def index(request):
    context = {}
    collection_slug = request.GET.get('collection')
    if not collection_slug:
        collection = Collection.get_default_collection()
        return redirect(f"{reverse('todolist:home')}?collection=_default")
    collection = get_object_or_404(Collection, slug=collection_slug)

    context['collections'] = Collection.objects.order_by('slug')
    context['current_collection'] = collection
    context['tasks'] = collection.task_set.all()

    return render(request, "todolist/index.html", context=context)


def get_tasks(request, collection_slug):
    context = {}
    collection = get_object_or_404(Collection, slug=collection_slug)
    context['current_collection'] = collection
    context['tasks'] = collection.task_set.all()
    context['collections'] = Collection.objects.order_by('slug')
    return render(request, "todolist/index.html", context=context)
    

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
