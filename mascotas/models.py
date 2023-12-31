from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime
from datetime import date
import os, random
from django.utils import timezone


# Create your models here.
class Mascota(models.Model):
    PERRO = 'Perro'
    GATO = 'Gato'
    CONEJO = 'Conejo'
    HAMSTER = 'Hamster'

    ANIMAL_CHOICES = [
        (PERRO, 'Perro'),
        (GATO, 'Gato'),
        (CONEJO, 'Conejo'),
        (HAMSTER, 'Hamster'),
    ]

    RAZA_CHOICES = {
        'Perro': [
            ('Chihuahua', 'Chihuahua'),
            ('Labrador', 'Labrador'),
            ('Salchicha (Dachshund)', 'Salchicha (Dachshund)'),
            ('Dálmata', 'Dálmata'),
            ('Bulldog', 'Bulldog'),
            ('Pastor Alemán', 'Pastor Alemán'),
            ('Golden Retriever', 'Golden Retriever'),
            ('Caniche', 'Caniche'),
            ('Boxer', 'Boxer'),
            ('Husky Siberiano', 'Husky Siberiano'),
            # ... otras razas de perros ...
        ],
        'Gato': [
            ('Siames', 'Siames'),
            ('Persa', 'Persa'),
            ('Maine Coon', 'Maine Coon'),
            ('Bengal', 'Bengal'),
            ('Sphynx', 'Sphynx'),
            ('Ragdoll', 'Ragdoll'),
            ('British Shorthair', 'British Shorthair'),
            ('Abyssinian', 'Abyssinian'),
            ('Scottish Fold', 'Scottish Fold'),
            ('Burmese', 'Burmese'),
            # ... otras razas de gatos ...
        ],
        'Conejo': [
            ('Holandes', 'Holandes'),
            ('Enano Holandes', 'Enano Holandes'),
            ('Cabeza de León', 'Cabeza de León'),
            ('Jersey Wooly', 'Jersey Wooly'),
            ('Rex', 'Rex'),
            ('Mini Rex', 'Mini Rex'),
            ('Californiano', 'Californiano'),
            ('Holland Lop', 'Holland Lop'),
            ('Flemish Giant', 'Flemish Giant'),
            ('Mini Lop', 'Mini Lop'),
            # ... otras razas de conejos ...
        ],
        'Hamster': [
            ('Dorado', 'Dorado'),
            ('Sirio', 'Sirio'),
            ('Roborovski', 'Roborovski'),
            ('Campbell', 'Campbell'),
            ('Chino', 'Chino'),
            # ... otras razas de hamsters ...
        ],
    }


    id_mascotas = models.AutoField(primary_key=True)
    rut_usuario = models.ForeignKey('mascotas.Usuario', related_name='mascotas', on_delete=models.CASCADE)
    nombre_m = models.CharField(max_length=100)
    animal_m = models.CharField(max_length=20, choices=ANIMAL_CHOICES)
    raza_m = models.CharField(max_length=50)
    genero_m = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], default='Macho')
    vacuna_m = models.BooleanField(default=False)
    fecha_nac_m = models.DateField()
    peso_m = models.FloatField()
    tamaño_m = models.CharField(max_length=20)
    color_m = models.CharField(max_length=50)
    comportamiento_m = models.TextField()
    imagen = models.ImageField(upload_to='uploads', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='uploads', blank=True, null=True)

    @classmethod
    def get_raza_choices(cls, animal):
        if animal == cls.PERRO:
            return [
                ('Chihuahua', 'Chihuahua'),
                ('Labrador', 'Labrador'),
                # ... otras razas de perros ...
            ]
        elif animal == cls.GATO:
            return [
                ('Siamés', 'Siamés'),
                ('Persa', 'Persa'),
                # ... otras razas de gatos ...
            ]
        elif animal == cls.CONEJO:
            return [
                ('Holandés', 'Holandés'),
                ('Enano Holandés', 'Enano Holandés'),
                # ... otras razas de conejos ...
            ]
        elif animal == cls.HAMSTER:
            return [
                ('Dorado', 'Dorado'),
                ('Sirio', 'Sirio'),
                # ... otras razas de hámsters ...
            ]
        else:
            return []

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