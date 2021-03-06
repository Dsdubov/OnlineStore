from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from .forms import CartAddProductForm
from bikeshop.models import Product
from django.core import serializers
from django.conf import settings 
from .cart import Cart
import json

from django.contrib import messages

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        ret = cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    if ret is False:
        if product.quantity <= 0:
            messages.add_message(request, messages.INFO, 'There is no {} now.'.format(product.name))
        else:
            messages.add_message(request, messages.INFO, 'Too much quantity choosen.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER',))

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True,})
    return render(request, 'cart/cart.html')
