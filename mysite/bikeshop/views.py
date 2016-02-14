from django.shortcuts import render
from .models import Catalog, Product, CatalogCategory
from django.http import HttpResponse

def index(request):
	return render(request, 'bikeshop/base.html')

def product_details(request):
	return render(request, 'bikeshop/product_detail.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'bikeshop/product_list.html', {'products': products})

def catalog_list(request):
	catalogs = Catalog.objects.all()
	return render(request, 'bikeshop/catalog_list.html', {'catalogs': catalogs})

def categories_list(request):
	categories = CatalogCategory.objects.filter(catalog=1)
	return render(request, 'bikeshop/categories_list.html', {'categories': categories})
