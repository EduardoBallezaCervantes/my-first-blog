from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=50)
    nombreEnfermedad = models.CharField( max_length=50)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    inicio_sintomas = models.DateTimeField()
    fin_sintomas = models.DateTimeField()
    vacunado = models.BooleanField()
   