# Generated by Django 3.2.10 on 2023-09-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='foto_de_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]