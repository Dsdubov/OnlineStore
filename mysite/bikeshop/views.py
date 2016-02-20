from django.shortcuts import render
from .models import *
from django.http import HttpResponse

dic = {"Bikes" : 1,
		"Bike Parts" : 2,
		"Bike Accessories" : 3,
		"Bike Clothing" : 4,
		}


def start(request):
	return render(request, 'bikeshop/start.html')

def register(request):
	return render(request, 'bikeshop/register.html')
	
def chart(request):
	return render(request, 'bikeshop/chart.html')

def pay(request):
	return render(request, 'bikeshop/pay.html')

def product_details(request, product_name):
	product = ProductDetail.objects.get(product__name=product_name)
	return render(request, 'bikeshop/product_detail.html', {'product' : product})

def product_list(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    return render(request, 'bikeshop/product_list.html', {'products': products})

def catalog_list(request):
	catalogs = Catalog.objects.all()
	return render(request, 'bikeshop/catalog_list.html', {'catalogs': catalogs})

def categories_list(request, catalog_name):
	categories = CatalogCategory.objects.filter(catalog__name=catalog_name)
	return render(request, 'bikeshop/categories_list.html', {'categories': categories})
