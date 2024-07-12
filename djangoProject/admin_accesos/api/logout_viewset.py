from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class LogoutAPIView(APIView):
    @staticmethod
    def post(request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
