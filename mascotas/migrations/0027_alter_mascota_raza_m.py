# Generated by Django 4.2.6 on 2023-12-31 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0026_alter_mascota_raza_m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='raza_m',
            field=models.CharField(blank=True, choices=[], max_length=50, verbose_name='Raza'),
        ),
    ]