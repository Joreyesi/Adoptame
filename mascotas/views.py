from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Importa la clase messages
from .forms import MascotaForm
from .models import Mascota, Usuario
from datetime import datetime


# Create your views here.
# En tu archivo views.py


def listado_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/listado_mascotas.html', {'mascotas': mascotas})


def ingresar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            # Crea un usuario ficticio o selecciona uno existente
            usuario, created = Usuario.objects.get_or_create(
                rut_usuario='usuario_ficticio',
                defaults={
                    'nombre_u': 'Usuario Ficticio',
                    'apellido_u': 'Ficticio',
                    'fecha_nac_u': datetime.now()  # Agrega la fecha de nacimiento actual o proporciona la fecha correcta
                }
            )
            # Asigna el usuario a la mascota
            mascota = form.save(commit=False)
            mascota.rut_usuario = usuario
            mascota.save()

            # Puedes agregar un mensaje de éxito
            messages.success(request, 'La mascota ha sido ingresada correctamente.')

            return redirect('listado_mascotas')
    else:
        form = MascotaForm()

    return render(request, 'mascotas/ingresar_mascota.html', {'form': form})




def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id_mascotas=mascota_id)
    mascota.delete()
    return redirect('listado_mascotas')