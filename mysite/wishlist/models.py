# from django.db import models
from decimal import Decimal
from django.conf import settings
from bikeshop.models import Product


class Wishlist(object):

    def __init__(self, request):
        """
        Initialize the wishlist.
        """
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)
        if not wishlist:
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = {}
        self.wishlist = wishlist

    def __len__(self):
        """
        Count all items in the wishlist.
        """
        return sum(1 for item in self.wishlist.values())

    def __iter__(self):
        """
        Iterate over the items in the wishlist and get the products from the database.
        """
        product_ids = self.wishlist.keys()
        products = Product.objects.filter(id__in=product_ids)
        # for product in products:
        #     self.wishlist[str(product.id)]['product'] = product

        for item in self.wishlist.values():
            yield item

    def add_remove(self, product):
        """
        Add or remove a product to the wishlist or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.wishlist:
            self.wishlist[product_id] = {'price': str(product.price_in_dollars)}
        else:
            del self.wishlist[product_id]
        self.save()


    def save(self):
        self.session[settings.WISHLIST_SESSION_ID] = self.wishlist
        # self.session.modified = True

    def clear(self):
        self.session[settings.WISHLIST_SESSION_ID] = {}
        # self.session.modified = True
        
    def get_product_ids(self):
        return self.wishlist.keys()

    def len(self):
        return sum(1 for item in self.wishlist.values())

