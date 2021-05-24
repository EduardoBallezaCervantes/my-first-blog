# Generated by Django 2.2.19 on 2021-05-24 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Sexo', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('inicio_sintomas', models.DateTimeField()),
                ('fin_sintomas', models.DateTimeField()),
                ('vacunado', models.BooleanField()),
            ],
        ),
    ]
