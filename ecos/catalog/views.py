from django.shortcuts import render
from django.http import HttpResponse
from .models import Catalog, Category
from django.core.paginator import Paginator

def index(request):
    catalog = Catalog.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(catalog, 12)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.page(page_num)
    context = {
        'title': 'Список',
        'categories': categories,
        'page_obj': page_objects,
    }
    return render(request, 'catalog/index.html', context)

def get_category(request, category_id):
    catalog = Catalog.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    paginator = Paginator(catalog, 12)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.page(page_num)
    context = {
        'categories': categories,
        'category': category,
        'page_obj': page_objects,
    }
    return render(request, 'catalog/category.html', context)

def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        catalog = Catalog.objects.filter(title__icontains=search_query)
    else:
        catalog = Catalog.objects.all()

    categories = Category.objects.all()
    paginator = Paginator(catalog, 12)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.page(page_num)
    context = {
        'title': 'Список',
        'categories': categories,
        'page_obj': page_objects,
        }
    return render(request, 'catalog/index.html', context)