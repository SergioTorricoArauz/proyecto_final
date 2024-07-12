from django.urls import path, include
from rest_framework import routers

from gasolineria.api import SurtidorViewset, BombaViewset, TipoCombustibleViewset, VentaViewset, VentasFechaView, \
    AnularVentaView, aumentar_stock_view

router = routers.DefaultRouter()

router.register(r'surtidor', SurtidorViewset)
router.register(r'bomba', BombaViewset)
router.register(r'tipocombustible', TipoCombustibleViewset)
router.register(r'venta', VentaViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('ventas_por_fecha/', VentasFechaView.as_view(), name='ventas_por_fecha'),
    path('anular_venta/<int:venta_id>/', AnularVentaView.as_view(), name='anular_venta'),
    path('aumentar_stock/', aumentar_stock_view, name='aumentar_stock'),
]
