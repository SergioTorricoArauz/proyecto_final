from django.urls import path, include
from rest_framework import routers

from app.api import CamionViewset, GetUsersAPIView, Recibirusuario, MostrarDatosAPIView, \
    recibir_notificacion_stock_agotado

router = routers.DefaultRouter()

router.register(r'camion', CamionViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('recibir-usuario/', Recibirusuario.as_view(), name='recibir-usuario'),
    path('ruta-para-obtener-usuarios/', GetUsersAPIView.as_view(), name='obtener-usuarios'),
    path('mostrar-datos/', MostrarDatosAPIView.as_view(), name='mostrar-datos'),
    path('notificacion_stock_agotado/', recibir_notificacion_stock_agotado, name='notificacion_stock_agotado'),
]
