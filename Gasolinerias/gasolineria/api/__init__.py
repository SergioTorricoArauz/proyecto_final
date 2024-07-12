from .simple_serializer import SurtidorSimpleSerializer, BombaSimpleSerializer, TipoCombustibleSimpleSerializer, \
    UserSimpleSerializer
from .surtidor_viewset import SurtidorViewset, SurtidorSerializer
from .bomba_viewset import BombaViewset, BombaSerializer
from .tipo_combustible_viewset import TipoCombustibleViewset, TipoCombustibleSerializer, aumentar_stock_view
from .venta_viewset import VentaViewset, VentaSerializer, VentasFechaView, AnularVentaView
