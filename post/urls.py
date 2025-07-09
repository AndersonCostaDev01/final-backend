# post/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoriaViewSet, ComentariosViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'comentarios', ComentariosViewSet, basename='comentarios')

urlpatterns = [
    path('', include(router.urls)),
]
