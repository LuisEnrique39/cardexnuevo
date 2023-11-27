# Generated by Django 3.2.10 on 2023-10-31 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps_cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded at')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Relaciones',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='batman.png', upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(choices=[('entrada oficina', 'ENTRADA OFICINA'), ('entrada homeofice', 'ENTRADA HOMEOFICE'), ('salida oficina', 'SALIDA OFICINA'), ('salida homeofice', 'SALIDA HOMEOFICE')])),
                ('activate', models.BooleanField(default=True, null=True)),
                ('fullname', models.CharField(max_length=200, null=True)),
                ('status', models.TextField(choices=[('A Tiempo', 'A Tiempo'), ('Retardo', 'Retardo')], default=True, null=True)),
                ('Fecha', models.CharField(max_length=200, null=True)),
                ('entrada', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Entradas/Salidas',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('telefono', models.CharField(max_length=250, null=True)),
                ('telefono_casa', models.CharField(max_length=250, null=True)),
                ('nacimiento', models.CharField(max_length=250, null=True)),
                ('direccion', models.CharField(max_length=300, null=True)),
                ('contacto_emergencia', models.CharField(max_length=250, null=True)),
                ('telefono_emergencia', models.CharField(max_length=250, null=True)),
                ('puesto', models.CharField(max_length=250, null=True)),
                ('departamento', models.CharField(max_length=250, null=True)),
                ('is_leader', models.BooleanField(default=False, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Informacion Personal',
            },
        ),
        migrations.CreateModel(
            name='DatosMedicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.CharField(max_length=250, null=True)),
                ('peso', models.CharField(max_length=250, null=True)),
                ('estatura', models.CharField(max_length=250, null=True)),
                ('alergias', models.CharField(max_length=500, null=True)),
                ('sangre', models.CharField(max_length=250, null=True)),
                ('enfermedad', models.CharField(max_length=300, null=True)),
                ('lentes', models.CharField(max_length=250, null=True)),
                ('fumas', models.CharField(max_length=250, null=True)),
                ('tomas', models.CharField(max_length=250, null=True)),
                ('deporte', models.CharField(max_length=250, null=True)),
                ('sueño', models.CharField(max_length=250, null=True)),
                ('covid', models.CharField(max_length=250, null=True)),
                ('vacuna', models.CharField(max_length=250, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='relationship',
            index=models.Index(fields=['from_user', 'to_user'], name='apps_client_from_us_09b8fc_idx'),
        ),
    ]