from django.urls import path, include
from rest_framework import serializers, routers
from .views import RegistroViewSet

router = routers.DefaultRouter()
router.register('ver_registros/',RegistroViewSet)

urlpatterns = [
    path('',include(router.urls))
]