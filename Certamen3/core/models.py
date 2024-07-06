from django.db import models
from django.contrib.auth.models import User


    

Turno=[
    ("AM","AM"),
    ("PM","PM"),
    ("AM","AM"),
]
    

class Registro(models.Model):
    CodigoCombustible= models.CharField(max_length=3)
    LitrosCombustible= models.CharField(max_length=50)
    FechaProduccion= models.CharField(max_length=50)
    DefinirTurno=models.CharField(max_length=50,choices=Turno)
    Horaregistro=models.CharField(max_length=300) 
    operador = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.CodigoCombustible
    