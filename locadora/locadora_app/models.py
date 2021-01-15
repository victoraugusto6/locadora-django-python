from django.db import models


# Create your models here.

class Filme(models.Model):
    titulo = models.TextField()
    capa = models.TextField()
    ano = models.IntegerField()
    diretor = models.TextField()
    sinopse = models.TextField()
    disponivel = models.BooleanField(default=False)
