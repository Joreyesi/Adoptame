# Generated by Django 4.2.6 on 2023-12-29 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0005_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]