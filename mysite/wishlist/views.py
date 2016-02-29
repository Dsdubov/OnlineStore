from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from bikeshop.models import Product
from .models import Wishlist
from django.http import HttpResponseRedirect

from cart.cart import Cart

def wishlist_button(request, product_id):
    wishlist = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wishlist.add_remove(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def wishlist_detail(request):
    wishlist = Wishlist(request)
    return render(request, 'wishlist/detail.html', {'wishlist': wishlist})
