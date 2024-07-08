from django.shortcuts import render
from rest_framework import serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Registro
from .serializers import RegistroSerializers
from .filters import RegistroFilter
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import action

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    #Gestión de la información a mostrar por el API
    serializer_class = RegistroSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['FechaProduccion']
    filterset_class = RegistroFilter

    @action(detail=False, methods=['get']) #Forma de extender vistas basadas en clases en Django REST Framework
    def suma_combustible(self, request):
        resultados = Registro.objects.values('planta','producto').annotate(total_combustible=Sum('LitrosCombustible'))
        data = [{'planta': resultado['planta'], 'total_combustible': resultado['total_combustible'], 'producto' : resultado['producto']} for resultado in resultados]
        return Response(data)

