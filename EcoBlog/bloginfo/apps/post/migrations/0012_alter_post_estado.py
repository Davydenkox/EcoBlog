# Generated by Django 3.2.9 on 2021-12-21 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_post_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='estado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]