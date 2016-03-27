from . import models
from cart.cart import Cart
from bikeshop.models import Catalog
from bikeshop.models import CatalogCategory

def categories_processor(request):
	categories = CatalogCategory.objects.all()
	return {'all_categories' : categories}

def catalogs_processor(request):
	catalogs = Catalog.objects.all()
	return {'catalogs' : catalogs}

def cart_processor(request):
	cart = Cart(request)
	return {'cart' : cart}


