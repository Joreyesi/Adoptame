# Generated by Django 4.2.6 on 2023-12-31 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0017_alter_mascota_genero_m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='raza_m',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
