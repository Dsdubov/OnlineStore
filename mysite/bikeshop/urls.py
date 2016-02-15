from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='base'),
    url(r'^catalog/([a-z A-Z]+)/categories/(?P<category_name>[a-z A-Z]+)/products/$', views.product_list, name='product_list'),
    url(r'^catalog/$', views.catalog_list, name='catalog_list'),
    url(r'^catalog/(?P<catalog_name>[a-z A-Z]+)/categories/$', views.categories_list, name='categories_list'),
    url(r'^catalog/([a-z A-Z]+)/categories/([a-z A-Z]+)/products/(?P<product_name>[a-z A-Z]+)/details/$', views.product_details, name='product_detail')
]