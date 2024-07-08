import django_filters
from core.models import Registro

class RegistroFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name='FechaProduccion', lookup_expr='year')
    month = django_filters.CharFilter(field_name='FechaProduccion', lookup_expr='month')

    class Meta:
        model = Registro
        fields = ['year', 'month']