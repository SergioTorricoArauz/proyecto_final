from django.contrib.auth.models import User
from rest_framework import serializers

from gasolineria.models import Bomba, Surtidor, TipoCombustible


class BombaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bomba
        fields = ['codigo']


class SurtidorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surtidor
        fields = ['nombre']


class TipoCombustibleSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCombustible
        fields = ['nombre']


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
