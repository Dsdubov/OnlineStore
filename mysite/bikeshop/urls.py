from django.conf.urls import url
import django
from . import views

urlpatterns = [
	url(r'^$', views.start, name='start'),
	url(r'^chart$', views.chart, name='chart'),
	url(r'^register$', views.register, name='registration'),
	url(r'^pay$', views.pay, name='pay'),
	url(r'^media/(?P<path>.*)$', django.views.static.serve, name='photo'),
    url(r'^catalog/([a-z A-Z 0-9]+)/categories/(?P<category_name>[a-z A-Z 0-9]+)/products/$', views.product_list, name='product_list'),
    url(r'^catalog/$', views.catalog_list, name='catalog_list'),
    url(r'^catalog/(?P<catalog_name>[a-z A-Z 0-9]+)/categories/$', views.categories_list, name='categories_list'),
    url(r'^catalog/([a-z A-Z 0-9]+)/categories/([a-z A-Z 0-9]+)/products/(?P<product_name>[a-z A-Z 0-9]+)/details/$', views.product_details, name='product_detail')
]