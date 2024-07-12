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
        return any(group in ['refineria-admin', 'refineria-driver'] for group in user_groups)


class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        logger.debug("Verificando permisos para SuperUserPermission")
        user_groups = getattr(request.user, 'groups', None)

        if user_groups is None or isinstance(user_groups, EmptyManager):
            logger.debug("user_groups es None o EmptyManager, asignando lista vacía")
            user_groups = []
        else:
            user_groups = list(user_groups)
            logger.debug(f"user_groups convertido a lista: {user_groups}")

        has_admin = 'refineria-admin' in user_groups
        logger.debug(f"Permiso de refineria-admin: {'Sí' if has_admin else 'No'}")
        return has_admin


class SuperUserPermission2(permissions.BasePermission):
    def has_permission(self, request, view):
        logger.debug("Verificando permisos para SuperUserPermission2")
        user_groups = getattr(request.user, 'groups', None)

        if user_groups is None or isinstance(user_groups, EmptyManager):
            logger.debug("user_groups es None o EmptyManager, asignando lista vacía")
            user_groups = []
        else:
            # Asegurarse de que user_groups es una lista, sin asumir que tiene el método .all()
            user_groups = list(user_groups.all()) if not isinstance(user_groups, EmptyManager) else []
            logger.debug(f"user_groups convertido a lista: {user_groups}")

        has_admin = 'refineria-admin' in user_groups
        logger.debug(f"Permiso de refineria-admin: {'Sí' if has_admin else 'No'}")
        return has_admin


class ChoferPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user_groups = getattr(request.user, 'groups', None)
        if user_groups is None or isinstance(user_groups, EmptyManager):
            user_groups = []
        else:
            user_groups = list(user_groups)
        return 'refineria-driver' in user_groups
