# Generated by Django 4.2.6 on 2023-12-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0006_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]