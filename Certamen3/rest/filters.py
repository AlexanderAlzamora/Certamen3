import django_filters
from core.models import Registro

class RegistroFilter(django_filters.FilterSet):
    Año = django_filters.NumberFilter(field_name='FechaProduccion', lookup_expr='year') #Esto permite filtrar por año (visto en StackOverflow)
    Mes = django_filters.CharFilter(field_name='FechaProduccion', lookup_expr='month') #Esto permite filtrar por mes (visto en StackOverflow)

    class Meta:
        model = Registro
        fields = ['Año', 'Mes']