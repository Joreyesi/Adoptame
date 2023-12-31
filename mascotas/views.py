from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import MascotaForm, SuperUsuarioForm, CustomUserCreationForm
from .models import Mascota, Usuario, MascotaAdoptada, SuperUsuario
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date
from django.http import HttpResponse
import uuid
from uuid import uuid4
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.utils import timezone


def home(request):
    context = {'user': request.user}
    return render(request, 'home.html', context)

@login_required(login_url='/user/login/')
def user_home(request):
    return render(request, 'user_home.html')



def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                # Intenta guardar el usuario
                form.save()
                # Resto de la lógica después de guardar el usuario
                return redirect('home')
            except IntegrityError:
                # Si hay una violación de la restricción única, el id_u ya existe
                form.add_error('id_u', 'Este ID de usuario ya está en uso.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registrar_usuario.html', {'form': form})

def registrar_superusuario(request):
    if request.method == 'POST':
        form = SuperUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Resto de la lógica después de guardar el superusuario
            return redirect('pagina_de_inicio')
    else:
        form = SuperUsuarioForm()
    
    return render(request, 'registrar_superusuario.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        id_u = request.POST['id_u']
        contraseña_u = request.POST['contraseña_u']
        user = authenticate(request, username=id_u, password=contraseña_u)

        if user is not None:
            login(request, user)
            return redirect('logeado')  # Redirige a la página deseada después del inicio de sesión
        else:
            # Manejar el caso en el que la autenticación falla
            return render(request, 'login.html', {'error_message': 'Usuario o contraseña incorrectos'})

    return render(request, 'login.html')  # Renderiza el formulario de inicio de sesión



def logeado(request):
    if request.method == 'POST':
        id_u = request.POST['id_u']
        password = request.POST['password']
        user = authenticate(request, id_u=id_u, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'logeado.html', {'user': user})
        else:
            # Manejar el caso en que la autenticación falla
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')

    return render(request, 'login.html')








def generar_id_u():
    return str(uuid4())


def listado_mascotas(request):
    mascotas_disponibles = Mascota.objects.exclude(id_mascotas__in=MascotaAdoptada.objects.values('mascota')).order_by('-fecha_nac_m')
    es_admin = request.user.is_authenticated and request.user.is_staff
    # Resto del código...
    return render(request, 'listado_mascotas.html', {'mascotas': mascotas_disponibles, 'es_admin': es_admin})





def ingresar_mascota(request):
    form = MascotaForm()  # Formulario vacío por defecto

    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        print(form.fields['raza_m'].choices)
        print(request.POST)
        print(request.FILES)
        
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.rut_usuario = request.user

            if mascota.imagen:
                try:
                    print("Antes de resize_image")
                    resize_image(mascota.imagen)
                    print("Después de resize_image")
                    
                    mascota.save()
                    messages.success(request, 'La mascota ha sido ingresada correctamente.')
                    return redirect('listado_mascotas')
                except ValidationError as e:
                    form.add_error(None, f'Error al ingresar la mascota: {e}')
            else:
                form.add_error('imagen', 'Error al ingresar la mascota. Por favor, sube una imagen.')
        else:
            print(form.errors)  # Agrega esta línea para imprimir los errores del formulario
            messages.error(request, 'Error al ingresar la mascota. Por favor, inténtalo de nuevo.')
    
    # Resto del código...

    return render(request, 'mascotas/ingresar_mascota.html', {'form': form})



def resize_image(image):
    print("Entré a resize_image")
    max_width = 600
    max_height = 300

    # Lee la imagen desde la memoria
    image_data = BytesIO(image.read())
    img = Image.open(image_data)
    
    # Redimensiona la imagen
    img.thumbnail((max_width, max_height))
    
    # Reinicia el puntero del objeto BytesIO al principio
    image_data.seek(0)
    
    # Guarda la imagen redimensionada en la memoria
    img.save(image_data, format='JPEG')  # Puedes ajustar el formato según tus necesidades

    # Crea un nuevo objeto de archivo para asignar al campo de imagen
    new_image = BytesIO()
    new_image.write(image_data.getvalue())
    new_image.seek(0)

    # Actualiza el campo de imagen con el nuevo objeto de archivo
    image.file = new_image
    image.name = f'resized_{image.name}'  # Puedes cambiar el nombre según tus necesidades

    return image

def detalle_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    return render(request, 'mascotas/detalle_mascota.html', {'mascota': mascota})



def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id_mascotas=mascota_id)
    mascota.delete()
    return redirect('listado_mascotas')





def adoptar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id_mascotas=mascota_id)

    # Verifica si la mascota no ha sido adoptada previamente
    if not hasattr(mascota, 'adoptada'):
        # Verifica si la mascota ha sido adoptada por otro usuario desde que se cargó la página
        if MascotaAdoptada.objects.filter(mascota=mascota).exists():
            messages.error(request, 'Esta mascota ya ha sido adoptada por otro usuario.')
            return redirect('listado_mascotas')

        # Crea una instancia de MascotaAdoptada
        mascota_adoptada = MascotaAdoptada.objects.create(
            mascota=mascota,
            fecha_adopcion=timezone.now(),
            adoptante_nombre=request.user.nombre_u,
            adoptante_rut=request.user.rut_usuario,
            ciudad_a=request.user.ciudad_u
        )

        # No elimines la mascota aquí, simplemente quítala de la lista mostrada
        # mascota.delete()

        # Redirige al listado de mascotas disponibles
        messages.success(request, '¡Felicidades! Has adoptado a {}'.format(mascota.nombre_m))
        return redirect('listado_mascotas')

    # Retorna algo en el caso en que la mascota ya ha sido adoptada
    messages.error(request, 'Esta mascota ya ha sido adoptada previamente.')
    return redirect('listado_mascotas')




def adoptar_mascota_lista(request):
    mascotas_adoptadas = MascotaAdoptada.objects.all()
    return render(request, 'mascotas/adoptar_mascota_lista.html', {'mascotas_adoptadas': mascotas_adoptadas})