# Generated by Django 3.2.10 on 2022-03-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='Categorias',
            field=models.ManyToManyField(to='productos.Categorias'),
        ),
    ]
