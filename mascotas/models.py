from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import datetime
import os

# Create your models here.
class Mascota(models.Model):
    id_mascotas = models.AutoField(primary_key=True)
    rut_usuario = models.ForeignKey('mascotas.Usuario', related_name='mascotas', on_delete=models.CASCADE)
    nombre_m = models.CharField(max_length=100)
    raza_m = models.CharField(max_length=100)
    vacuna_m = models.BooleanField(default=False)
    tipo_m = models.CharField(max_length=100)
    genero_m = models.CharField(max_length=10)
    fecha_nac_m = models.DateField()
    tamaño_m = models.CharField(max_length=20)
    color_m = models.CharField(max_length=50)
    comportamiento_m = models.TextField()
    peso_m = models.FloatField()
    especie_m = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='uploads', blank=True, null=True)

    class Meta:
        app_label = 'mascotas'

    def __str__(self):
        return self.nombre_m
    

class MascotaAdoptada(models.Model):
    id_adoptada = models.AutoField(primary_key=True)
    mascota = models.OneToOneField(Mascota, related_name='adoptada', on_delete=models.CASCADE)
    fecha_adopcion = models.DateField()

    class Meta:
        app_label = 'mascotas'

    def __str__(self):
        return f"{self.mascota.nombre_m} - Adoptada el {self.fecha_adopcion}"
    



class Usuario(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    rut_usuario = models.CharField(max_length=12, primary_key=True)
    nombre_u = models.CharField(max_length=100)
    apellido_u = models.CharField(max_length=100)
    genero_u = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    fecha_nac_u = models.DateField(default=datetime.date.today)
    id_u = models.CharField(max_length=20, unique=True, null=True, blank=True)
    contraseña_u = models.CharField(max_length=128)  # Campo para contraseñas hash
    telefono_u = models.CharField(max_length=15)
    ciudad_u = models.CharField(max_length=100)
    
    # Cambiar related_name para evitar conflictos con 'auth.User'
    groups = models.ManyToManyField(Group, related_name='usuarios_related_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_related_permissions', blank=True)

    def __str__(self):
        return f"{self.nombre_u} {self.apellido_u}"

class SuperUsuario(AbstractUser):
    rut_superusuario = models.CharField(max_length=12, primary_key=True)
    nombre_su = models.CharField(max_length=100)
    apellido_su = models.CharField(max_length=100)
    genero_su = models.CharField(max_length=10)
    fecha_nac_su = models.DateField(default=datetime.date.today)
    id_su = models.CharField(max_length=20, unique=True, null=True, blank=True)
    contraseña_su = models.CharField(max_length=128)  # Campo para contraseñas hash
    telefono_su = models.CharField(max_length=15)
    ciudad_su = models.CharField(max_length=100)
    
    # Cambiar related_name para evitar conflictos con 'auth.User'
    groups = models.ManyToManyField(Group, related_name='superusuarios_related_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='superusuarios_related_permissions', blank=True)

    def __str__(self):
        return f"{self.nombre_su} {self.apellido_su}"



class Organizacion(models.Model):
    id_org_o = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('mascotas.Usuario', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
    personal_o = models.IntegerField()
    mascotas_o = models.IntegerField()
    ciudad_o = models.CharField(max_length=100)
    calle_o = models.CharField(max_length=255)
    tipo_personal_o = models.CharField(max_length=50)
    tipo_mascotas_o = models.CharField(max_length=50)
    n_calle_o = models.CharField(max_length=10)
    cantidad_mascotas_o = models.IntegerField()

    def __str__(self):
        return f"Organización #{self.id_org_o}"
    
class Estado(models.Model):
    id_mascotas_e = models.AutoField(primary_key=True)
    id_mascota = models.ForeignKey('mascotas.Mascota', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
    vacunas_e = models.BooleanField()
    tipo_vacuna_e = models.CharField(max_length=50, blank=True, null=True)
    tratamiento_e = models.TextField(blank=True, null=True)
    historial_medico_e = models.TextField(blank=True, null=True)
    nutricion_e = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Estado de mascota #{self.id_mascotas_e}"
    

class Publicacion(models.Model):
    id_p = models.AutoField(primary_key=True)
    id_org_o = models.ForeignKey('mascotas.Organizacion', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
    nombres_p = models.CharField(max_length=100)
    nombre_mascota_p = models.CharField(max_length=100)
    fecha_p = models.DateField()
    comentario_p = models.TextField()
    cantidad_p = models.IntegerField()

    def __str__(self):
        return f"Publicación #{self.id_p}"
    

class Galeria(models.Model):
    id_galeria = models.AutoField(primary_key=True)
    id_mascota = models.ForeignKey('mascotas.Mascota', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
    cantidad_fotos_g = models.IntegerField()
    descripcion_g = models.TextField(blank=True, null=True)
    tipo_mascota_g = models.CharField(max_length=50)
    perfil_g = models.BooleanField(default=False)

    def __str__(self):
        return f"Galería de mascota #{self.id_galeria}"
    

class Comuna(models.Model):
    nombre_c = models.CharField(max_length=100, primary_key=True)
    nombre_r = models.ForeignKey('mascotas.Region', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
    rut_usuario = models.ForeignKey('mascotas.Usuario', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
    id_org_o = models.ForeignKey('mascotas.Organizacion', on_delete=models.CASCADE, blank=True, null=True)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.

    def __str__(self):
        return self.nombre_c
    

class Region(models.Model):
    nombre_r = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.nombre_r