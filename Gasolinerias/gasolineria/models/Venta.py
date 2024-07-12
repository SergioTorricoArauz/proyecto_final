from django.db import models
from gasolineria.models import TipoCombustible, Bomba


class Venta(models.Model):
    ESTADO_COMPLETADA = 1
    ESTADO_ANULADO = 2

    ESTADO_CHOICES = (
        (ESTADO_COMPLETADA, 'Aceptado'),
        (ESTADO_ANULADO, 'Anulado'),
    )

    nombre_factura = models.CharField(max_length=100)
    nit_factura = models.CharField(max_length=50)
    cliente = models.CharField(max_length=100)
    correo = models.EmailField()
    monto = models.FloatField()
    precio_actual_producto = models.FloatField(null=True, blank=True)
    cantidad_producto_litros = models.FloatField(null=True, blank=True)
    tipo_producto = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True, blank=True)
    estado = models.IntegerField(choices=ESTADO_CHOICES, default=ESTADO_COMPLETADA)

    def save(self, *args, **kwargs):
        self.precio_actual_producto = self.tipo_producto.precio
        if self.precio_actual_producto > 0:
            self.cantidad_producto_litros = self.monto / self.precio_actual_producto
        else:
            self.cantidad_producto_litros = 0
        super(Venta, self).save(*args, **kwargs)

    @property
    def estado_display(self):
        return dict(self.ESTADO_CHOICES).get(self.estado, 'Unknown')

    def __str__(self):
        return self.nombre_factura
