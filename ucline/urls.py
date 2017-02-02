"""ucline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from redsocial.views import *


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'timeline', TimelineViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'resource', ResourceViewSet)
router.register(r'profile', ProfileViewsSet)
router.register(r'Area_Conocimiento', Area_ConocimientoViewsSet)
router.register(r'canal', CanalViewsSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^entities/', include(router.urls)),
    url(r'^', include('redsocial.urls')),
]

