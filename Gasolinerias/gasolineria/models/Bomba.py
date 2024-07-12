from django.db import models

from gasolineria.models import Surtidor


class Bomba(models.Model):
    codigo = models.CharField(max_length=50)
    surtidor = models.ForeignKey(Surtidor, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo
