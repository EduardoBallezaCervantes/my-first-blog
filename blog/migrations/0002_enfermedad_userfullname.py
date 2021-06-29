# Generated by Django 2.2.19 on 2021-06-22 20:52

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFullName',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombreEnfermedad', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('inicio_sintomas', models.DateTimeField()),
                ('fin_sintomas', models.DateTimeField()),
                ('vacunado', models.BooleanField()),
                ('enfermedadesUsuario', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
