from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'East Asia'
    }
    return render(request, 'menu/index.html', context)


def products(request):
    context = {
        'title': 'East Asia - Каталог'
    }
    return render(request, 'menu/products.html', context)


def test_context(request):
    context = {
        'title': 'East Asia',
        'header': 'Добро пожаловать!',
        'username': 'Адико Ж',
        'products': [
            {'name': 'Жаркое', 'price': '450'},
            {'name': 'Лагман', 'price': '400'},
            {'name': 'Плов с говядиной', 'price': '350'},
        ],
        # 'promotion': True,
        'products_of_promotion': [

        ]
    }
    return render(request, 'menu/test_context.html', context)