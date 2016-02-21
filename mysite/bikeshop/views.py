from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate 
from django.template import RequestContext
from django.shortcuts import render_to_response

def start(request):
    return render(request, 'bikeshop/start.html')

# def register(request):
#     return render(request, 'bikeshop/register.html')
    
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

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'bikeshop/login.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # TODO:
#             # 1. создать пользователя,
#             # 2. установить ему пароль
#             # 3. Зайти под его именем на сайт
#             return HttpResponseRedirect('/')

#     else:
#         form = RegistrationForm()
#     return render(request, 'bikeshop/reg.html', {'form': form})


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'bikeshop/reg.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)