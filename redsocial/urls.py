from django.conf.urls import include, url
from redsocial.views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^index', index, name='index'),
]



