# Generated by Django 5.0.6 on 2024-07-11 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('chofer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('lalitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Preparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('litros_combustible', models.FloatField()),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.camion')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_entregada', models.FloatField()),
                ('precio_litro', models.FloatField()),
                ('preparacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.preparacion')),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ruta')),
            ],
        ),
    ]
