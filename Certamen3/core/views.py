
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Registro,Planta,Producto
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .forms import RegistroForm

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
            return redirect('agregar_produccion') 
        else:
            return render(request, 'core/login.html')
    else:
        return render(request, 'core/login.html')
    
@login_required 
def logout_view(request):
        logout(request)
        return redirect('home')


def registrar_produccion(request):
    registros = Registro.objects.filter(operador=request.user)

    # Mostrar los registros
    
    if request.method == 'POST':
        
        litros_producidos = request.POST.get('txtProduccion')
        turno = request.POST.get('eleccionTurno')
        fecha_produccion = request.POST.get('txtfecha')
        hora_registro = request.POST.get('txtHora')
        planta_id = request.POST.get('planta')
        producto_id = request.POST.get('producto')
        operador = request.user  # Asumiendo que el operador es el usuario actual

        # Verificar que planta_id y producto_id estén presentes y sean válidos
        if planta_id and producto_id:
                planta = Planta.objects.get(id=planta_id)
                producto = Producto.objects.get(id=producto_id)
                
                registro = Registro(
                    
                    LitrosCombustible=litros_producidos,
                    DefinirTurno=turno,
                    FechaProduccion=fecha_produccion,
                    Horaregistro=hora_registro,
                    operador=operador,
                    planta=planta,
                    producto=producto
                )
                registro.save()
                return render(request, 'core/VerProduccion.html', {'registros': registros})

    plantas = Planta.objects.all()
    productos = Producto.objects.all()
    return render(request, 'core/ingresar_produccion.html', {'plantas': plantas, 'productos': productos})

def ver_produccion(request):
    # Recuperar todos los registros del usuario autenticado
    registros = Registro.objects.filter(operador=request.user)

    # Mostrar los registros
    return render(request, 'core/VerProduccion.html', {'registros': registros})

def editar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk) #Obtiene un objeto específico del modelo Registro según su clave primaria
    if request.method == "POST": #Si coloca todos los datos entra al if, sino lo envia nuevamente al formulario
        registros = Registro.objects.filter(operador=request.user)
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return render(request, 'core/VerProduccion.html', {'registros': registros})
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'core/editar_registro.html', {'form': form})