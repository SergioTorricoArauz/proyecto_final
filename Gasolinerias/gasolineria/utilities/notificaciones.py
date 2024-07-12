import requests
from django.conf import settings


def notificar_stock_agotado(surtidor_nombre, bomba_nombre):
    url = settings.NOTIFICACION_API_URL  # La URL de la API a la que se enviará la notificación
    token = settings.NOTIFICACION_API_TOKEN  # Obtén el token de las configuraciones
    payload = {
        'surtidor': surtidor_nombre,
        'bomba': bomba_nombre,
        'mensaje': 'El stock de combustible se ha agotado.'
    }
    headers = {
        'Authorization': f'Bearer {token}',  # Añade el token al encabezado de autorización
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Esto lanzará una excepción para respuestas de error HTTP
    except requests.RequestException as e:
        # Manejar errores en la solicitud HTTP
        print(f"Error al enviar la notificación: {e}")
