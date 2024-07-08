from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import requests
from django.conf import settings
import datetime
from dateutil import parser

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
        # Después de guardar, enviamos la notificación a Slack
        self.enviar_notificacion_slack()
    
    #Esto es para obtener todo lo que contenga el modelo producto y el operador
    def __str__(self):
        return  f"{self.producto} - {self.operador}"
        
    def enviar_notificacion_slack(self):
        webhook_url = settings.SLACK_WEBHOOK_URL
        if not webhook_url:
            print("No se ha configurado el webhook de Slack.")
            return

        # Parseamos la fecha y hora si son strings
        if isinstance(self.FechaProduccion, str):
            self.FechaProduccion = parser.parse(self.FechaProduccion).date()
        if isinstance(self.Horaregistro, str):
            self.Horaregistro = parser.parse(self.Horaregistro).time()

        # Se combinamos la fecha y la hora
        fecha_hora = datetime.datetime.combine(self.FechaProduccion, self.Horaregistro).strftime('%d-%m-%Y %H:%M')

        # Se arma el mensaje
        mensaje = (

            f"{fecha_hora} – Nuevo Registro de Producción – de "
            f"{self.LitrosCombustible} lts. en "
            f"{self.planta}"
        )

        # Preparamos el payload para Slack
        payload = {"text": mensaje}

        # Enviamos la solicitud POST a Slack
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 200:
            print(f"Error al enviar la notificación a Slack: {response.status_code}, {response.text}")
        else:
            print("Notificación enviada exitosamente a Slack.")