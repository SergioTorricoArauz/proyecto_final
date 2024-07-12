import logging

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from app.auth import SuperUserPermission

logger = logging.getLogger(__name__)


class GetUsersAPIView(APIView):
    permission_classes = [SuperUserPermission]

    @staticmethod
    def post(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if auth_header is None:
            return Response({"error": "Token de autorización no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

        headers = {'Authorization': auth_header}
        url = "http://127.0.0.1:8000/api/ruta-para-listar-usuarios/"
        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status()
            users_data = response.json()
            logger.info(f"Datos recibidos de la API externa: {users_data}")
        except requests.RequestException as e:
            logger.error(f"Error making the request to the external API: {e}")
            return Response({"error": "Error connecting to the external API"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            logger.error(f"Error deserializing the response from the external API: {e}")
            return Response({"error": "Error deserializing the response from the external API"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Verificar y formatear los datos recibidos antes de enviarlos
        if 'message' in users_data:
            # Si la respuesta contiene un mensaje, envíelo directamente
            return Response({"datos_recibidos": users_data['message']}, status=status.HTTP_200_OK)
        else:
            # Si la respuesta contiene otros datos, envíelos como están
            return Response({"datos_recibidos": users_data}, status=status.HTTP_200_OK)


class Recibirusuario(APIView):
    permission_classes = [SuperUserPermission]

    datos_procesados = []  # Class variable to store processed data

    @classmethod
    def post(cls, request):
        datos_recibidos = request.data
        if not isinstance(datos_recibidos, list):
            logger.error("Formato de datos incorrecto. Se esperaba una lista.")
            return Response({"error": "Formato de datos incorrecto. Se esperaba una lista."},
                            status=status.HTTP_400_BAD_REQUEST)

        for item in datos_recibidos:
            logger.info(f"Procesando item: {item}")
            cls.datos_procesados.append(item)  # Save the processed item to the class variable

        logger.info("Procesamiento de datos completado. Enviando respuesta.")
        return Response({"mensaje": "Datos recibidos y procesados correctamente"}, status=status.HTTP_200_OK)


class MostrarDatosAPIView(APIView):
    permission_classes = [SuperUserPermission]
    # Asumiendo que datos_procesados es accesible de alguna manera, por ejemplo, como un atributo de clase
    datos_procesados = []

    def get(self, request, *args, **kwargs):
        return Response({'datos': self.datos_procesados})
