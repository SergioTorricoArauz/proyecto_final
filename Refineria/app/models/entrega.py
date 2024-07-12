from django.db import models

from app.models import Ruta, Preparacion


class Entrega(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    preparacion = models.ForeignKey(Preparacion, on_delete=models.CASCADE)
    cantidad_entregada = models.FloatField()
    precio_litro = models.FloatField()
