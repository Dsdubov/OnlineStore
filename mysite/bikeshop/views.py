import re
from .models import *
from cart.cart import Cart
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponse
from wishlist.models import Wishlist
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from cart.forms import CartAddProductForm
from django.views.generic import ListView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate 
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

def start(request):
    return render(request, 'bikeshop/start.html')
    
def cart(request):
    return render(request, 'bikeshop/cart.html')

def pay(request):
    return render(request, 'bikeshop/pay.html')

def product_details(request, product_name):
    wishlist = Wishlist(request)
    if wishlist:
        wishlist_ids = [int(x) for x in wishlist.get_product_ids()]
    else:
        wishlist_ids = []
    product = ProductDetail.objects.get(product__name=product_name)
    cart_product_form = CartAddProductForm()
    comment_form = CommentForm()
    return render(request, 'bikeshop/product_detail.html', {'product' : product, 'cart_product_form': cart_product_form, 'wishlist' : wishlist, 'wishlist_ids' : wishlist_ids, 'comment_form' : comment_form})

def product_list(request, category_name):
    wishlist = request.session.get(settings.WISHLIST_SESSION_ID)
    if wishlist:
        wishlist_ids = [int(x) for x in wishlist.keys()]
    else:
        wishlist_ids = []
    # cart = Cart(request)
    products = Product.objects.filter(category__name=category_name)
    category = CatalogCategory.objects.get(name=category_name)
    cart_product_form = CartAddProductForm()
    return render(request, 'bikeshop/product_list.html', {'products': products, 'cart_product_form': cart_product_form, 'catalog' : category.catalog, 'category' : category, 'wishlist' : wishlist_ids})

def catalog_list(request):
    catalogs = Catalog.objects.all()
    return render(request, 'bikeshop/catalog_list.html', {'catalogs': catalogs})

def categories_list(request, catalog_name):
    categories = CatalogCategory.objects.filter(catalog__name=catalog_name)
    return render(request, 'bikeshop/categories_list.html', {'categories': categories, 'catalog' : catalog_name})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user_name = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()
    return render(request, 'bikeshop/product_detail.html', {'comment_form': form, 'product' : product})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('blog.views.product_detail', pk=comment.product.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product_pk = comment.product.pk
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('blog.views.product_detail', pk=product_pk)

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            subject = 'Registration'
            mail = user.email
            message = 'Dear {},\nThank you for registration on buybike.pythonanywhere.com!.'.format(user.username)
            mail_sent = EmailMessage(subject, message, to=[mail,])
            mail_sent.send()
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render_to_response(
            'bikeshop/register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('bikeshop/login.html', {}, context)

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    cart_product_form = CartAddProductForm()
    wishlist = request.session.get(settings.WISHLIST_SESSION_ID)
    if wishlist:
        wishlist_ids = [int(x) for x in wishlist.keys()]
    else:
        wishlist_ids = []
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['name', 'description', 'manufacturer'])
        
        found_entries = Product.objects.filter(entry_query).order_by('-price_in_dollars')

    return render_to_response('bikeshop/search.html',
                          { 'query_string': query_string, 'found_entries': found_entries, 'wishlist_ids' :wishlist_ids, 'cart_product_form' : cart_product_form }, context_instance=RequestContext(request))

