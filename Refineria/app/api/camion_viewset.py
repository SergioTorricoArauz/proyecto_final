import logging

from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from app.auth import SuperUserPermission
from app.models import Camion


class CamionSerializer(serializers.ModelSerializer):
    chofer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Camion
        fields = '__all__'


class CamionViewset(viewsets.ModelViewSet):
    serializer_class = CamionSerializer
    queryset = Camion.objects.all()
    permission_classes = [SuperUserPermission]
