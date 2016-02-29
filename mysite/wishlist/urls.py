from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.wishlist_detail, name='wishlist_detail'),
    url(r'^add_remove/(?P<product_id>\d+)/$', views.wishlist_button, name='wishlist_button'),
]
