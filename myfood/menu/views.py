from django.shortcuts import render

from menu.models import MenuCategory, Menu

# Create your views here.

def index(request):
    context = {
        'title': 'East Asia'
    }
    return render(request, 'menu/index.html', context)


def products(request):
    context = {
        'title': 'East Asia - Каталог',
        'categories': MenuCategory.objects.all(),
        'Menu': Menu.objects.all(),
    }
    return render(request, 'menu/products.html', context)
