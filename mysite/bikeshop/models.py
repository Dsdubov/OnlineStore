from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from django.contrib.auth import login

class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('CatalogCategory', related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.FileField(upload_to='product_photo', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_in_dollars = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name

class CatalogCategory(models.Model):        
   catalog = models.ForeignKey('Catalog', related_name='categories')
   parent = models.ForeignKey('self', blank=True, null=True, related_name='children')        
   name = models.CharField(max_length=300)
   slug =  models.SlugField(max_length=150)
   description = models.TextField(blank=True)
   def __str__(self):
        return self.name

class ProductDetail(models.Model):
    '''
    The ``ProductDetail`` model represents information unique to a 
    specific product. This is a generic design that can be used 
    to extend the information contained in the ``Product`` model with 
    specific, extra details.
    '''
    product = models.ForeignKey('Product', related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    def __str__(self):
        return str(self.product)

class ProductAttribute(models.Model):
    '''
    The ``ProductAttribute`` model represents a class of feature found 
    across a set of products. It does not store any data values 
    related to the attribute, but only describes what kind of a 
    product feature we are trying to capture. Possible attributes 
    include things such as materials, colors, sizes, and many, many 
    more.
    '''
    name = models.CharField(max_length=300)
    materials = models.CharField(max_length=300)
    # colors = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'Повторите пароль', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # TODO: проверить, что username не занят
        return self.cleaned_data

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # TODO: проверить, что пароли совпадают
        return self.cleaned_data

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.FileField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')