
from django.urls import path

from django.conf.urls import url
from . import views
from .views import newsletter_signup, newsletter_unsubcribe


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sitemap/$', views.sitemap, name='sitemap'),
    url(r'^fbaform/$', views.fbaForm, name='fbaform'),
    path('signup/', newsletter_signup, name='newsletter_signup'),
    path('unsubscribe/', newsletter_unsubcribe, name='newsletter_unsubcribe'),
]

