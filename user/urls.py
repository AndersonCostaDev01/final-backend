from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, UserSearchViewSet

# Rota manual para UserProfileViewSet (perfil individual)
user_profile = UserProfileViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy',
})

# Router só para busca múltipla
router = DefaultRouter()
router.register(r'buscar-usuarios', UserSearchViewSet, basename='buscar')

urlpatterns = [
    path('profile/<str:pk>/', user_profile, name='user-detail'), # /users/<username>/
    path('', include(router.urls)),                             # /users/search/buscar-usuarios/?search=...
]