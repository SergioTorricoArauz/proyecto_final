import logging

logger = logging.getLogger(__name__)


def procesar_notificacion_stock_agotado(data):
    try:
        surtidor = data.get('surtidor')
        bomba = data.get('bomba')
        mensaje = data.get('mensaje')

        # Realiza las acciones necesarias con los datos recibidos.
        # Por ejemplo, registrar un log, enviar una alerta, etc.
        logger.info(f"Notificación recibida: Surtidor={surtidor}, Bomba={bomba}, Mensaje={mensaje}")

        # Aquí podrías agregar más lógica, como guardar en una base de datos, enviar un correo, etc.
        return {'status': 'Notificación procesada correctamente.'}
    except Exception as e:
        return {'error': str(e)}



