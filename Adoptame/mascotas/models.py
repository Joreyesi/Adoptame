from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Mascota(models.Model):
    id_mascotas = models.AutoField(primary_key=True)
    rut_usuario = models.ForeignKey('Adoptame.Usuario', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
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

    def __str__(self):
        return self.nombre_m
    

    class Usuario(AbstractUser):
    rut_usuario = models.CharField(max_length=12, primary_key=True)
    nombre_u = models.CharField(max_length=100)
    apellido_u = models.CharField(max_length=100)
    genero_u = models.CharField(max_length=10)
    fecha_nac_u = models.DateField()
    id_u = models.CharField(max_length=20, unique=True)
    contraseña_u = models.CharField(max_length=100)  # Considera utilizar un campo más seguro para contraseñas en un entorno de producción.
    telefono_u = models.CharField(max_length=15)
    ciudad_u = models.CharField(max_length=100)
    tipo_usuario_u = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre_u} {self.apellido_u}"
    

    class Organizacion(models.Model):
    id_org_o = models.AutoField(primary_key=True)
    rut_usuario = models.ForeignKey('Adoptame.Usuario', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
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
    id_mascota = models.ForeignKey('Adoptame.Mascota', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
    vacunas_e = models.BooleanField()
    tipo_vacuna_e = models.CharField(max_length=50, blank=True, null=True)
    tratamiento_e = models.TextField(blank=True, null=True)
    historial_medico_e = models.TextField(blank=True, null=True)
    nutricion_e = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Estado de mascota #{self.id_mascotas_e}"
    

    class Publicacion(models.Model):
    id_p = models.AutoField(primary_key=True)
    id_org_o = models.ForeignKey('Adoptame.Organizacion', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
    nombres_p = models.CharField(max_length=100)
    nombre_mascota_p = models.CharField(max_length=100)
    fecha_p = models.DateField()
    comentario_p = models.TextField()
    cantidad_p = models.IntegerField()

    def __str__(self):
        return f"Publicación #{self.id_p}"
    
