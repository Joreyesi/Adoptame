# Generated by Django 4.2.6 on 2023-12-30 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0010_remove_superusuario_contraseña_su_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superusuario',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
