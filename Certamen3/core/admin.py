from django.contrib import admin


from .models import Registro,Planta,Producto

admin.site.register(Registro)
admin.site.register(Planta)
admin.site.register(Producto)#registrar el modelo mensaje en django
# Register your models here.
