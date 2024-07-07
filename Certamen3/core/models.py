from django.db import models
from django.contrib.auth.models import User
class Producto(models.Model):
    codigo= models.CharField(max_length=3)
    nombre = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre

class Planta(models.Model):
    codigo= models.CharField(max_length=3)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    TURNO_CHOICES = [
        ('AM', 'Mañana'),
        ('PM', 'Tarde'),
        ('MM', 'Noche'),
    ]

    CodigoCombustible = models.CharField(max_length=100)
    LitrosCombustible = models.FloatField()
    DefinirTurno = models.CharField(max_length=2, choices=TURNO_CHOICES)
    FechaProduccion = models.DateField()
    Horaregistro = models.TimeField()
    operador = models.ForeignKey(User, on_delete=models.CASCADE)
    planta = models.ForeignKey('Planta', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)

    def __str__(self):
        return self.CodigoCombustible