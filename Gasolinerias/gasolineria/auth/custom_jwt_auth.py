from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication, exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.exceptions import InvalidToken
from gasolineria.auth import CustomAuthUser


class CustomJWTAuth(authentication.BaseAuthentication):
    jwt_auth = JWTAuthentication()

    def authenticate(self, request):
        token_str = request.headers.get('Authorization', '')[7:]
        if not token_str:
            return AnonymousUser(), None
        try:
            token = self.jwt_auth.get_validated_token(token_str)
        except InvalidToken:
            raise exceptions.AuthenticationFailed('Invalid Token')
        self.check_groups(token)
        return self.get_custom_user(token), None

    @staticmethod
    def check_groups(token):
        groups = token.get('groups', [])
        if not any(group in groups for group in ['surtidor-admin', 'surtidor-seller', 'speruser']):
            raise exceptions.AuthenticationFailed('Unauthorized group')

    @staticmethod
    def get_custom_user(token):
        user_id = token['user_id']
        user_name = token['user']
        groups = token.get('groups', [])
        if not isinstance(groups, list):
            groups = []  # Asegura que groups sea siempre una lista

        custom_user = CustomAuthUser()
        custom_user.groups = groups
        custom_user.pk = user_id
        custom_user.username = user_name  # Añade el nombre de usuario al CustomAuthUser
        custom_user.is_authenticated = True
        return custom_user
