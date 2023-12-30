# Generated by Django 4.2.6 on 2023-12-30 00:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('mascotas', '0009_alter_superusuario_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superusuario',
            name='contraseña_su',
        ),
        migrations.AddField(
            model_name='superusuario',
            name='is_staff',
            field=models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.'),
        ),
        migrations.AlterField(
            model_name='superusuario',
            name='fecha_nac_su',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='superusuario',
            name='groups_su',
            field=models.ManyToManyField(blank=True, related_name='superusuarios_related_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='superusuario',
            name='user_permissions_su',
            field=models.ManyToManyField(blank=True, related_name='superusuarios_related_permissions', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nac_u',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
