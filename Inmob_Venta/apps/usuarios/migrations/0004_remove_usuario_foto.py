# Generated by Django 3.2.10 on 2022-04-12 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuario_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='foto',
        ),
    ]