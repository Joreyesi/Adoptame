# Generated by Django 4.2.6 on 2023-12-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0021_alter_mascota_raza_m'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascotaadoptada',
            name='ciudad_a',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]