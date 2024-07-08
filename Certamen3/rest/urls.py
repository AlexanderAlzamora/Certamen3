from django.urls import path, include
from rest_framework import serializers, routers
from . import views
from .views import RegistroViewSet

router = routers.DefaultRouter()
router.register('ver_registros/',views.RegistroViewSet)

#path('', SumaCombustiblePorPlanta.as_view(), name='suma-combustible'),

urlpatterns = [
    path('',include(router.urls))
]