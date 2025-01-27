from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from app.utilities import procesar_notificacion_stock_agotado


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recibir_notificacion_stock_agotado(request):
    resultado = procesar_notificacion_stock_agotado(request.data)
    if 'error' in resultado:
        return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
    return Response(resultado, status=status.HTTP_200_OK)
