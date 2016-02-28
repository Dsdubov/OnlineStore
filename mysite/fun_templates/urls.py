from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.quick_look, name='quick_look'),
]