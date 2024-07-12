# Generated by Django 5.0.6 on 2024-07-11 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surtidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bomba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('surtidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gasolineria.surtidor')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCombustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('stock', models.FloatField()),
                ('bomba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gasolineria.bomba')),
                ('surtidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gasolineria.surtidor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_factura', models.CharField(max_length=100)),
                ('nit_factura', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('monto', models.FloatField()),
                ('precio_actual_producto', models.FloatField(blank=True, null=True)),
                ('cantidad_producto_litros', models.FloatField(blank=True, null=True)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('estado', models.IntegerField(choices=[(1, 'Completada'), (2, 'Anulado')], default=1)),
                ('bomba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gasolineria.bomba')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gasolineria.tipocombustible')),
            ],
        ),
    ]
