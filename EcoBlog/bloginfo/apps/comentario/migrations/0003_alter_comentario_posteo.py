# Generated by Django 3.2.9 on 2021-12-20 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20211214_1811'),
        ('comentario', '0002_comentario_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='posteo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]