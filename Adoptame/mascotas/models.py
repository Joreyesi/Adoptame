from django.db import models

# Create your models here.
class Mascota(models.Model):
    id_mascotas = models.AutoField(primary_key=True)
    rut_usuario = models.ForeignKey('TuApp.Usuario', on_delete=models.CASCADE)  # Asegúrate de reemplazar 'TuApp' con el nombre real de tu aplicación.
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