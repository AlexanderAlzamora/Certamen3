
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Registro
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render


def index(request):
    return render(request,'core/index.html')


@login_required
def home_view(request):
    return render(request, 'core/base.html')


   
def Sesion(request):
    if request.method == 'POST': #El usuario envía el formulario de inicio de sesión eso por el metodo post
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username, password=password)#verifica credenciales
        
        if user is not None:
            login(request, user)
            if  user.is_staff:
                return redirect('/proyectos')   #si son correctas y el usario es profesor redirecciona a proyectos
            else:
                 return redirect('/Ingresar_produccion') #si son correctas y el usuario es alumno redirecciona a ingresar un nuevo proyecto
        else:
            return render(request, 'core/proyectos.html')
    else:
        return render(request, 'core/login.html')
    
@login_required 
def logout_view(request):
        logout(request)
        return redirect('home')

def nuevo_proyecto(request):
    return render(request, 'core/ingresar_produccion.html')


def agregar_proyecto(request):
        if(request.POST):
            Codigo= request.POST['txtCombustible']
            Litros=request.POST['txtProduccion']
            escogerturno= request.POST['eleccionTurno']
            Fecha=request.POST['txtfecha']
            Hora=request.POST['txtHora']   
            operador = request.user         

            registro=Registro()
            registro.CodigoCombustible=Codigo
            registro.LitrosCombustible=Litros
            registro.DefinirTurno=escogerturno
            registro.FechaProduccion=Fecha
            registro.Horaregistro=Hora
            registro.operador = operador
            #guardar cambio en la base de datos
            registro.save()

        return render(request,'core/ingresar_produccion.html')

def ver_produccion(request):
    # Recuperar todos los registros del usuario autenticado
    registros = Registro.objects.filter(operador=request.user)

    # Mostrar los registros
    return render(request, 'core/VerProduccion.html', {'registros': registros})