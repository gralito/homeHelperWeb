from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.utils.text import slugify

from todolist.models import Collection

# Create your views here.
def index(request):
    collections = Collection.objects.order_by('slug')
    return render(request, "todolist/index.html", context={
        "collections": collections,
    })


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
