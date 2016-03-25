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
    photo = models.FileField(upload_to='bikeshop/media/catalog_photo', blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name


class CatalogCategory(models.Model):        
   catalog = models.ForeignKey('Catalog', related_name='categories')
   parent = models.ForeignKey('self', blank=True, null=True, related_name='children')        
   name = models.CharField(max_length=300)
   slug =  models.SlugField(max_length=150)
   description = models.TextField(blank=True)
   photo = models.FileField(upload_to='bikeshop/media/category_photo', blank=True)
   def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('CatalogCategory', related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.FileField(upload_to='bikeshop/media/product_photo', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_in_dollars = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
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
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey('Product', related_name='comment')
    user_name = models.ForeignKey(User)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.FileField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
