# Generated by Django 4.2.6 on 2023-12-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_remove_superusuario_tipo_usuario_su_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nac_u',
            field=models.DateField(),
        ),
    ]