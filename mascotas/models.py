from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime
from datetime import date
import os, random
from django.utils import timezone


# Create your models here.
class Mascota(models.Model):
    id_mascotas = models.AutoField(primary_key=True)
    rut_usuario = models.ForeignKey('mascotas.Usuario', related_name='mascotas', on_delete=models.CASCADE)
    nombre_m = models.CharField(max_length=100)

    
    ANIMAL_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Conejo', 'Conejo'),
        ('Hámster', 'Hámster'),
        # Agrega otros animales si es necesario
    ]

    RAZA_CHOICES = {
        'Perro': [
            ('Chihuahua', 'Chihuahua'),
            ('Labrador', 'Labrador'),
            # Otras razas de perros
        ],
        'Gato': [
            ('Siamés', 'Siamés'),
            ('Persa', 'Persa'),
            # Otras razas de gatos
        ],
        'Conejo': [
            ('Holandés', 'Holandés'),
            ('Enano Holandés', 'Enano Holandés'),
            # Otras razas de conejos
        ],
        'Hámster': [
            ('Dorado', 'Dorado'),
            ('Sirio', 'Sirio'),
            # Otras razas de hámsters
        ],
    }

    animal_m = models.CharField(max_length=20, choices=ANIMAL_CHOICES, default='Perro')
    raza_m = models.CharField(max_length=50, choices=[], blank=True)
    genero_m = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], default='Macho')
    vacuna_m = models.BooleanField(default=False)

    fecha_nac_m = models.DateField()
    peso_m = models.FloatField()
    tamaño_m = models.CharField(max_length=20)
    color_m = models.CharField(max_length=50)
    comportamiento_m = models.TextField()
    imagen = models.ImageField(upload_to='uploads', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='uploads', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Configurar las opciones de raza_m según el tipo de animal
        raza_options = Mascota.RAZA_CHOICES.get(self.animal_m, [])
        self.raza_m = ""
        if raza_options:
            self.raza_m = raza_options[0][0]  # Establece el valor predeterminado como la primera opción
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_m} ({self.animal_m} - {self.raza_m} - {self.genero_m})"
    
    class Meta:
        app_label = 'mascotas'


    

class MascotaAdoptada(models.Model):
    id_adoptada = models.AutoField(primary_key=True)
    mascota = models.OneToOneField(Mascota, related_name='adoptada', on_delete=models.CASCADE)
    fecha_adopcion = models.DateField()
    adoptante_nombre = models.CharField(max_length=255, blank=True, null=True)
    adoptante_rut = models.CharField(max_length=20, blank=True, null=True)
    ciudad_a = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'mascotas'

    def __str__(self):
        return f"{self.mascota.nombre_m} - Adoptada el {self.fecha_adopcion}"
    

class UsuarioManager(BaseUserManager):
    def create_user(self, id_u, email, password=None, **extra_fields):
        if not id_u:
            raise ValueError('El campo ID de usuario es obligatorio')

        email = self.normalize_email(email)
        user = self.model(id_u=id_u, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_u, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(id_u, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    CITY_CHOICES = [
        ('Iquique', 'Iquique'),
        ('Alto Hospicio', 'Alto Hospicio'),
    ]

    rut_usuario = models.CharField(max_length=12, primary_key=True)
    nombre_u = models.CharField(max_length=100)
    apellido_u = models.CharField(max_length=100)
    genero_u = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    fecha_nac_u = models.DateField(default=timezone.now)
    id_u = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    telefono_u = models.CharField(max_length=15)
    ciudad_u = models.CharField(max_length=100, choices=CITY_CHOICES)  # Utiliza las opciones específicas

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'id_u'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return f"{self.nombre_u} {self.apellido_u}"

class SuperUsuario(Usuario):
    rut_superusuario = models.CharField(max_length=12, primary_key=True)
    nombre_su = models.CharField(max_length=100)
    apellido_su = models.CharField(max_length=100)
    genero_su = models.CharField(max_length=10)
    fecha_nac_su = models.DateField(default=timezone.now)
    id_su = models.CharField(max_length=20, unique=True, null=True, blank=True)
    telefono_su = models.CharField(max_length=15)
    ciudad_su = models.CharField(max_length=100)

    groups_su = models.ManyToManyField('auth.Group', related_name='superusuarios_related_groups', blank=True)
    user_permissions_su = models.ManyToManyField('auth.Permission', related_name='superusuarios_related_permissions', blank=True)


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