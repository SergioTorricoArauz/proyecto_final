from datetime import datetime

from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

from gasolineria.api import TipoCombustibleSimpleSerializer, BombaSimpleSerializer
from gasolineria.auth import GroupPermission, SuperUserPermission
from gasolineria.models import Venta, Bomba, TipoCombustible

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class VentaSerializer(serializers.ModelSerializer):
    estado_display = serializers.SerializerMethodField()
    tipo_producto = TipoCombustibleSimpleSerializer(read_only=True)
    tipo_producto_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoCombustible.objects.all(),
        source='tipo_producto',
        write_only=True)
    bomba = BombaSimpleSerializer(read_only=True)
    bomba_id = serializers.PrimaryKeyRelatedField(
        queryset=Bomba.objects.all(),
        source='bomba',
        write_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'nombre_factura', 'cliente', 'correo', 'monto', 'precio_actual_producto',
                  'cantidad_producto_litros', 'tipo_producto',
                  'tipo_producto_id',
                  'bomba', 'bomba_id', 'fecha_hora', 'estado_display']

    @staticmethod
    def get_estado_display(obj):
        return obj.get_estado_display()

    def create(self, validated_data):
        tipo_producto = validated_data['tipo_producto']
        monto = validated_data['monto']
        precio_actual_producto = tipo_producto.precio
        if precio_actual_producto > 0:
            cantidad_producto_litros = monto / precio_actual_producto
        else:
            raise serializers.ValidationError("El precio del producto no puede ser cero o negativo.")
        tipo_producto.reducir_stock(cantidad_producto_litros)
        validated_data['cantidad_producto_litros'] = cantidad_producto_litros
        venta = Venta.objects.create(**validated_data)
        return venta


class VentaViewset(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    permission_classes = [GroupPermission]

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Método no permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Método no permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Método no permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class VentasFechaView(APIView):
    permission_classes = [SuperUserPermission]

    @staticmethod
    def get(request):
        logger.debug("Entrando a VentasFechaView")

        # Verificar los permisos del usuario
        logger.debug(f"Usuario: {request.user}")
        try:
            logger.debug(f"Grupos del usuario: {[group.name for group in request.user.groups.all()]}")
        except AttributeError as e:
            logger.debug(f"Error obteniendo los grupos del usuario: {e}")

        fecha = request.query_params.get('fecha')
        if not fecha:
            return Response({'error': 'Falta la fecha en los parámetros de la URL.'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Formato de fecha incorrecto. Debe ser YYYY-MM-DD.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            ventas = Venta.objects.filter(fecha_hora__date=fecha).order_by('-fecha_hora')
            if not ventas.exists():
                return Response({'error': 'No hay ventas para la fecha proporcionada.'},
                                status=status.HTTP_404_NOT_FOUND)

            serializer = VentaSerializer(ventas, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error al obtener las ventas: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AnularVentaView(APIView):
    permission_classes = [SuperUserPermission]

    @staticmethod
    def post(request, venta_id):
        try:
            venta = Venta.objects.get(id=venta_id)
            if venta.estado == Venta.ESTADO_ANULADO:
                return Response({'error': 'La venta ya está anulada.'}, status=status.HTTP_400_BAD_REQUEST)

            # Reponer el stock de combustible
            tipo_combustible = venta.tipo_producto
            tipo_combustible.aumentar_stock(venta.cantidad_producto_litros)
            tipo_combustible.save()

            # Anular la venta
            venta.estado = Venta.ESTADO_ANULADO
            venta.save()

            return Response({'mensaje': 'Venta anulada y stock repuesto correctamente.'}, status=status.HTTP_200_OK)
        except Venta.DoesNotExist:
            return Response({'error': 'Venta no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error al anular la venta: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
