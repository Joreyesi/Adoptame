# Generated by Django 4.2.6 on 2023-12-29 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0007_usuario_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='is_staff',
        ),
    ]
