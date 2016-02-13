from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='base'),
    url(r'^products$', views.product_list, name='product_list'),
    url(r'^catalog$', views.catalog_list, name='catalog_list'),
    url(r'^categories$', views.categories_list, name='categories_list'),
]