from django.shortcuts import render
from .models import Catalog, Product
# from django.http import HttpResponse


def product_list(request):
    products = Product.objects.all()
    return render(request, 'bikeshop/base.html', {'products': products})