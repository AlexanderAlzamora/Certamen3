from rest_framework import serializers
from core.models import Registro
class RegistroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['planta', 'LitrosCombustible','producto']
