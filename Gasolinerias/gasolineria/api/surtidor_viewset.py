from rest_framework import serializers, viewsets
from rest_framework.decorators import permission_classes

from gasolineria.auth import SuperUserPermission
from gasolineria.models import Surtidor


class SurtidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surtidor
        fields = '__all__'


@permission_classes([SuperUserPermission])
class SurtidorViewset(viewsets.ModelViewSet):
    serializer_class = SurtidorSerializer
    queryset = Surtidor.objects.all()
