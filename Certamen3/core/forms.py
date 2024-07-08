from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['producto', 'LitrosCombustible', 'FechaProduccion', 'DefinirTurno', 'Horaregistro'] #Almacena los datos que estan dentro del modelo Registro y permite utilizarlos