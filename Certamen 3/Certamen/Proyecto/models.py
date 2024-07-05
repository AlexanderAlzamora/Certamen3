from django.db import models

# Create your models here.
Turnito=[
    ("AM","AM"),
    ("PM","PM"),
    ("MM","MM"),
]



#Class Carrera
class Registro(models.Model):
    codigoCombustible = models.CharField(max_length=10)
    litrosCombustibles = models.CharField(max_length=80)
    Fecha = models.IntegerField()
    Turno = models.CharField(max_length=80,choices=Turnito)
    hora = models.CharField(max_length=80)



    def __str__(self) -> str:
       return self.Turno