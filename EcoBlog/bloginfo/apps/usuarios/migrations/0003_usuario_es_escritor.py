# Generated by Django 3.2.9 on 2021-12-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_es_administrador'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='es_escritor',
            field=models.BooleanField(default=False),
        ),
    ]