from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fun/', include('fun_templates.urls')),
    url(r'^wishlist/', include('wishlist.urls', namespace="wishlist")),
    url(r'^cart/', include('cart.urls', namespace="cart")),
    url(r'^orders/', include('orders.urls', namespace='orders')),    
    url(r'^', include('bikeshop.urls', namespace="bikeshop")),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
