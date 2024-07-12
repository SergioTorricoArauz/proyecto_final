from rest_framework import permissions
import logging

from django.db.models.manager import EmptyManager

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class GroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user_groups = getattr(request.user, 'groups', None)
        if user_groups is None or isinstance(user_groups, EmptyManager):
            user_groups = []
        else:
            user_groups = list(user_groups)
        return any(group in ['surtidor-admin', 'surtidor-seller'] for group in user_groups)


class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        logger.debug("Verificando permisos para SuperUserPermission")

        # Verificar si el usuario está autenticado
        if not request.user.is_authenticated:
            logger.debug("Usuario no autenticado")
            return False

        user_groups = getattr(request.user, 'groups', [])
        if isinstance(user_groups, list):
            user_groups = user_groups
        else:
            user_groups = [group.name for group in user_groups.all()]  # Extraer nombres de grupos si no es una lista
        logger.debug(f"user_groups convertido a lista de nombres: {user_groups}")

        has_admin = 'surtidor-admin' in user_groups
        logger.debug(f"Permiso de surtidor-admin: {'Sí' if has_admin else 'No'}")
        return has_admin


class ChoferPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if any(group == 'refineria-driver' for group in request.user.groups):
            return True
        return False
