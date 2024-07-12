from django.db import models

from gasolineria.models import Surtidor, Bomba
from gasolineria.utilities import notificar_stock_agotado


class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=50)
    surtidor = models.ForeignKey(Surtidor, on_delete=models.CASCADE)
    bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    precio = models.FloatField(blank=True, null=True)
    stock = models.FloatField(default=0.0)

    def reducir_stock(self, cantidad):
        if self.stock is not None and self.stock >= cantidad:
            self.stock -= cantidad
            self.save()
            if self.stock < 10:
                notificar_stock_agotado(self.surtidor.nombre, self.bomba.codigo)
        else:
            raise ValueError("La cantidad a reducir es mayor que el stock disponible.")

    def aumentar_stock(self, cantidad):
        if self.stock is None:
            self.stock = 0.0
        self.stock += cantidad
        self.save()

    def __str__(self):
        return self.nombre
