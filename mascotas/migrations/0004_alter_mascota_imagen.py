# Generated by Django 4.2.6 on 2023-12-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0003_mascota_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='mascotas\\uploads'),
        ),
    ]
