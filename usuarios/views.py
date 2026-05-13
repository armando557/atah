from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q

from .forms import RegistroForm
from .models import Registro


def registro_usuario(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Ese usuario ya existe'
            )

            return redirect('registro_usuario')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            'Cuenta creada correctamente'
        )

        return redirect('login')

    return render(request, 'registro_usuario.html')

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('inicio')

        else:

            messages.error(
                request,
                'Usuario o contraseña incorrectos'
            )

    return render(request, 'login.html')


# =========================
# INICIO
# =========================

@login_required
def inicio(request):

    return render(request, 'inicio.html')


# =========================
# REGISTRO DE OPERADORES
# =========================

@login_required
def registro(request):

    if request.method == 'POST':

        form = RegistroForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('inicio')

    else:

        form = RegistroForm()

    return render(request, 'registro.html', {
        'form': form
    })


# =========================
# BUSCAR OPERADORES
# =========================

@login_required
def buscar_operadores(request):

    buscar = request.GET.get('buscar')

    operadores = Registro.objects.all()

    if buscar:

        operadores = operadores.filter(

            Q(nombre__icontains=buscar) |
            Q(alias__icontains=buscar) |
            Q(curp__icontains=buscar) |
            Q(rfc__icontains=buscar) |
            Q(telefono__icontains=buscar) |
            Q(ciudad__icontains=buscar) |
            Q(licencia__icontains=buscar) |
            Q(socio__icontains=buscar)

        )

    return render(request, 'buscar.html', {
        'operadores': operadores
    })

# =========================
# EDITAR OPERADOR
# =========================

@login_required
def editar_operador(request, id):

    operador = Registro.objects.get(id=id)

    if request.method == 'POST':

        form = RegistroForm(
            request.POST,
            request.FILES,
            instance=operador
        )

        if form.is_valid():

            form.save()

            return redirect('buscar')

    else:

        form = RegistroForm(
            instance=operador
        )

    return render(request, 'editar.html', {
        'form': form,
        'operador': operador
    })


# =========================
# ELIMINAR OPERADOR
# =========================

@login_required
def eliminar_operador(request, id):

    operador = Registro.objects.get(id=id)

    operador.delete()

    return redirect('buscar')


# =========================
# PERFIL SECRETARIA
# =========================

@login_required
def perfil(request):

    return render(request,
    'perfil.html',
    {
        'usuario': request.user
    })


# =========================
# VALIDACIONES
# =========================

@login_required
def validaciones(request):

    pendientes = Registro.objects.filter(
        estado='Revision'
    )

    return render(
        request,
        'validaciones.html',
        {
            'pendientes': pendientes
        }
    )


# =========================
# NOTIFICACIONES
# =========================

@login_required
def notificaciones(request):

    registros = Registro.objects.order_by('-id')[:10]

    return render(
        request,
        'notificaciones.html',
        {
            'registros': registros
        }
    )


# =========================
# CERRAR SESION
# =========================

def cerrar_sesion(request):

    logout(request)

    return redirect('login')