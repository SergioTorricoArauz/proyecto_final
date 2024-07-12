from django.db import models

from app.models import Camion


class Preparacion(models.Model):
    nombre = models.CharField(max_length=10)
    litros_combustible = models.FloatField()
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
