# Generated by Django 5.2 on 2025-04-08 10:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('precio_inicial', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01, message='El precio debe ser mayor que 0')])),
                ('valoracion', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(1.0, message='La valoración debe ser al menos 1.0'), django.core.validators.MaxValueValidator(5.0, message='La valoración no puede ser mayor a 5.0')])),
                ('stock', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='El stock debe ser al menos 1')])),
                ('marca', models.CharField(max_length=100)),
                ('imagen', models.URLField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_cierre', models.DateTimeField()),
                ('estado', models.CharField(choices=[('abierta', 'Abierta'), ('cerrada', 'Cerrada')], default='abierta', max_length=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subastas', to='subastas.categoria')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Puja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_puja', models.DateTimeField(auto_now_add=True)),
                ('pujador', models.CharField(max_length=100)),
                ('subasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pujas', to='subastas.subasta')),
            ],
            options={
                'ordering': ('-fecha_puja',),
            },
        ),
    ]
