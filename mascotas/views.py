from django.shortcuts import render, redirect
from django.contrib import messages  # Importa la clase messages
from .forms import MascotaForm
from .models import Mascota


# Create your views here.
# En tu archivo views.py


def listado_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/listado_mascotas.html', {'mascotas': mascotas})


def ingresar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            # Agrega un mensaje de éxito
            messages.success(request, 'La mascota fue ingresada correctamente.')
            return redirect('listado_mascotas')
    else:
        form = MascotaForm()

    return render(request, 'mascotas/ingresar_mascota.html', {'form': form})