from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import MascotaForm, UsuarioForm, SuperUsuarioForm
from .models import Mascota, Usuario, MascotaAdoptada, SuperUsuario
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.http import HttpResponse
import uuid
from uuid import uuid4
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'home.html')

@login_required(login_url='/user/login/')
def user_home(request):
    return render(request, 'user_home.html')



def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Resto de la lógica después de guardar el usuario
            return redirect('home')
    else:
        form = UsuarioForm()
    
    return render(request, 'user_login.html', {'form': form})

def registrar_superusuario(request):
    if request.method == 'POST':
        form = SuperUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Resto de la lógica después de guardar el superusuario
            return redirect('home')
    else:
        form = SuperUsuarioForm()
    
    return render(request, 'admin_login.html', {'form': form})


def generar_id_u():
    return str(uuid4())


def listado_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/listado_mascotas.html', {'mascotas': mascotas})




def ingresar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            rut_usuario = generar_id_u()  # Usa la función generar_id_u
            usuario, created = Usuario.objects.get_or_create(
                rut_usuario=rut_usuario,
                defaults={
                    'nombre_u': 'Usuario Ficticio',
                    'apellido_u': 'Ficticio',
                    'fecha_nac_u': datetime.now(),
                    'id_u': rut_usuario  # Asigna el valor de rut_usuario a id_u
                }
            )
            mascota = form.save(commit=False)
            mascota.rut_usuario = usuario
            mascota.save()

            messages.success(request, 'La mascota ha sido ingresada correctamente.')

            return redirect('listado_mascotas')
    else:
        form = MascotaForm()

    return render(request, 'mascotas/ingresar_mascota.html', {'form': form})





def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id_mascotas=mascota_id)
    mascota.delete()
    return redirect('listado_mascotas')



def adoptar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id_mascotas=mascota_id)

    # Verifica si la mascota no ha sido adoptada previamente
    if not hasattr(mascota, 'adoptada'):
        # Crea una instancia de MascotaAdoptada
        mascota_adoptada = MascotaAdoptada.objects.create(
            mascota=mascota,
            fecha_adopcion=date.today()
        )

        # Corrige el nombre del espacio de nombres en la función reverse
        url = reverse('mascotas:adoptar_mascota_lista')  # Cambia a tu nombre de URL real
        return redirect(url)

    # Retorna algo en el caso en que la mascota ya ha sido adoptada
    return HttpResponse("Esta mascota ya ha sido adoptada previamente.")



def adoptar_mascota_lista(request):
    mascotas_adoptadas = MascotaAdoptada.objects.all()
    return render(request, 'mascotas/adoptar_mascota_lista.html', {'mascotas_adoptadas': mascotas_adoptadas})