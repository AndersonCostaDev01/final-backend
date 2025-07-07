# user/urls.py

from django.urls import path
from .views import UserProfileViewSet

# Ações do ViewSet baseadas na rota
user_profile = UserProfileViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('<str:pk>/', user_profile, name='user-detail'),  # /users/<username>/
]
