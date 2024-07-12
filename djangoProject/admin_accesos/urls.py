from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from admin_accesos.api import LogoutAPIView, CreateUserView, CustomTokenObtainPairView, \
    ListUsersView  # Importa CreateUserView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # opcional
    path('api-token-auth/', views.obtain_auth_token),
    path('auth/logout/', LogoutAPIView.as_view(), name='auth_logout'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),  # Agrega la ruta para crear usuarios

    path('ruta-para-listar-usuarios/', ListUsersView.as_view(), name='list_users'),

]
