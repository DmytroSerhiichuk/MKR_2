from django.shortcuts import render, get_object_or_404
from .models import Category

def gallery_view(request):
    data = {
        'categories' : Category.objects.all()
    }
    return render(request, 'gallery.html', context=data)

def image_detail(request, pk):
    ...
