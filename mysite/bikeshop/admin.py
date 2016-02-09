from django.contrib import admin
from .models import Catalog, Product, CatalogCategory

admin.site.register(Catalog)
admin.site.register(Product)
admin.site.register(CatalogCategory)

# Register your models here.
