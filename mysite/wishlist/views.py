from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bikeshop.models import Product
from .models import Wishlist
from django.http import HttpResponseRedirect
from django.conf import settings

def wishlist_button(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wishlist.add_remove(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def wishlist_detail(request):
    wishlist = Wishlist(request)
    if wishlist:
	    wishlist_ids = [int(x) for x in wishlist.get_product_ids()]
    else:
    	wishlist_ids = []
    return render(request, 'wishlist/detail.html', {'wishlist': wishlist, 'wishlist_ids' : wishlist_ids})
