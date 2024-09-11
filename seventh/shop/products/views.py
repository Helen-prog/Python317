from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    return render(request, 'products/index.html', {'title': 'Market Place'})


def products(request, category_id=None):
    context = {
        'title': 'Market Place - Каталог',
        'categories': ProductCategory.objects.all(),
        # 'products': Product.objects.all()
    }
    if category_id:
        context.update({
            'products': Product.objects.filter(category_id=category_id)
        })
    else:
        context.update({
            'products': Product.objects.all()
        })
    return render(request, 'products/products.html', context)
