from django.db import models


class Ruta(models.Model):
    nombre = models.CharField(max_length=10)
    lalitud = models.FloatField()
    longitud = models.FloatField()
