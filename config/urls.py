"""MountainAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import UserViewSet, AreaViewSet, MountainPassViewSet, submitData, mountain_get
from config.yasg import urlpatterns as swagger_urls

router = routers.DefaultRouter()
router.register('MountainPass', MountainPassViewSet)
router.register(r'user', UserViewSet)
router.register(r'area', AreaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/submitData/', submitData),
    path('api/<int:mountain_pass_id>', mountain_get)
]

urlpatterns += swagger_urls
