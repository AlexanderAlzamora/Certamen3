from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

    producto = models.ForeignKey('Producto', on_delete=models.CASCADE) #Si el objeto es eliminado, también se eliminará el objeto que contiene la clave externa.
    LitrosCombustible = models.FloatField(verbose_name="Litros de Combustible Cargados")
    DefinirTurno = models.CharField(max_length=2, choices=TURNO_CHOICES, verbose_name="Turno")
    FechaProduccion = models.DateField(verbose_name="Fecha de Produccion")
    Horaregistro = models.TimeField(verbose_name="Hora de Registro")
    operador = models.ForeignKey(User, on_delete=models.CASCADE)
    planta = models.ForeignKey('Planta', on_delete=models.CASCADE)
    UltimaEdicion = models.DateTimeField(null=True, blank=True) #Esto permite guardar cuando fue la ultima mod.

    #Actualiza automáticamente la UltimaEdicion con la fecha 
    # y hora actuales cada vez que se guarda el objeto en la base de datos, para completar el proceso de guardado estándar.
    def save(self, *args, **kwargs):
        self.UltimaEdicion = timezone.now()
        super().save(*args, **kwargs)
    
    #Esto es para obtener todo lo que contenga el modelo producto y el operador
    def __str__(self):
        return  f"{self.producto} - {self.operador}"