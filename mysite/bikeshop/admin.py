from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Catalog)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price_in_dollats', 'manufacturer']
    list_filter = ['price_in_dollats', 'category']
    list_editable = ['price_in_dollats']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product)
admin.site.register(CatalogCategory)
admin.site.register(ProductDetail)
admin.site.register(ProductAttribute)

# Register your models here.
