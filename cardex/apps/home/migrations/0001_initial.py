# Generated by Django 3.2.10 on 2023-09-26 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=500)),
                ('costo_por_hora', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(blank=True, max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=255)),
                ('ciudad', models.CharField(blank=True, max_length=100)),
                ('pais', models.CharField(blank=True, max_length=100)),
                ('codigo_postal', models.IntegerField(blank=True, null=True)),
                ('about_me', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionPuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('precio_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.actividad')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.proyecto')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.puesto')),
            ],
        ),
    ]
