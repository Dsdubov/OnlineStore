from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
import django
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^search/$', views.search, name='search'),    
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^login/$', views.user_login, name='log_in'),
	url(r'^add_comment/(?P<product_id>\d+)/$', views.add_comment, name='add_comment'),
	url(r'^register/$', views.register, name='registration'),
	url(r'^cart/$', views.cart, name='chart'),
	url(r'^pay/$', views.pay, name='pay'),
	url(r'^media/(?P<path>.*)$', django.views.static.serve, name='photo'),
    url(r'^catalogs/$', views.catalog_list, name='catalog_list'),
    url(r'^(?P<catalog_name>[a-z A-Z 0-9]+)/categories/$', views.categories_list, name='categories_list'),
    url(r'^(?P<category_name>[a-z A-Z 0-9]+)/products/$', views.product_list, name='product_list'),
    url(r'^(?P<product_name>[a-z A-Z 0-9]+)/details/$', views.product_details, name='product_detail'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)