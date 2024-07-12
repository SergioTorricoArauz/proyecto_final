from django.http import JsonResponse
from rest_framework import serializers, viewsets
from rest_framework.decorators import permission_classes, api_view


from gasolineria.api import SurtidorSimpleSerializer, BombaSimpleSerializer
from gasolineria.auth import SuperUserPermission, ChoferPermission
from gasolineria.models import TipoCombustible, Surtidor, Bomba


class TipoCombustibleSerializer(serializers.ModelSerializer):
    surtidor = SurtidorSimpleSerializer(read_only=True)
    surtidor_id = serializers.PrimaryKeyRelatedField(
        queryset=Surtidor.objects.all(),
        source='surtidor',
        write_only=True)
    bomba = BombaSimpleSerializer(read_only=True)
    bomba_id = serializers.PrimaryKeyRelatedField(
        queryset=Bomba.objects.all(),
        source='bomba',
        write_only=True)

    class Meta:
        model = TipoCombustible
        fields = '__all__'


@permission_classes([SuperUserPermission])
class TipoCombustibleViewset(viewsets.ModelViewSet):
    serializer_class = TipoCombustibleSerializer
    queryset = TipoCombustible.objects.all()


@api_view(['POST'])
@permission_classes([ChoferPermission])
def aumentar_stock_view(request):
    try:
        tipo_combustible_id = request.data.get('tipo_combustible_id')
        cantidad = request.data.get('cantidad')

        if not tipo_combustible_id or not cantidad:
            return JsonResponse({'error': 'Faltan datos necesarios.'}, status=400)

        tipo_combustible = TipoCombustible.objects.get(pk=tipo_combustible_id)
        tipo_combustible.aumentar_stock(float(cantidad))

        return JsonResponse({'mensaje': 'Stock actualizado correctamente.'})
    except TipoCombustible.DoesNotExist:
        return JsonResponse({'error': 'TipoCombustible no encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
