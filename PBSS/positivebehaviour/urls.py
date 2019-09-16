
from django.urls import path

from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^sitemap/$', views.sitemap, name='sitemap'),
    url(r'^index/$', views.index, name='index')
]
