from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Importa la clase messages
from .forms import MascotaForm
from .models import Mascota, Usuario, MascotaAdoptada
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date



# Create your views here.
# En tu archivo views.py


def listado_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/listado_mascotas.html', {'mascotas': mascotas})


def ingresar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES
        if form.is_valid():
            usuario, created = Usuario.objects.get_or_create(
                rut_usuario='usuario_ficticio',
                defaults={
                    'nombre_u': 'Usuario Ficticio',
                    'apellido_u': 'Ficticio',
                    'fecha_nac_u': datetime.now()
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
    # Revertir la URL a través del nombre del espacio de nombres
        url = reverse('mascotas:listado_mascotas')
        return redirect(url)



def adoptar_mascota_lista(request):
    mascotas_adoptadas = MascotaAdoptada.objects.all()
    return render(request, 'mascotas/adoptar_mascota_lista.html', {'mascotas_adoptadas': mascotas_adoptadas})