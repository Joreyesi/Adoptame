# Generated by Django 4.2.6 on 2023-12-25 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0008_alter_mascota_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='MascotaAdoptada',
            fields=[
                ('id_adoptada', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_adopcion', models.DateField()),
                ('mascota', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adoptada', to='mascotas.mascota')),
            ],
        ),
    ]