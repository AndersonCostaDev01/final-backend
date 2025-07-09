# post/views.py

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Categoria, Comentario
from .serializers import PostSerializer, CategoriaSerializer, ComentarioSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # GET /posts/por-categoria/<categoria_id>/
    @action(detail=False, methods=['get'], url_path='por-categoria/(?P<categoria_id>[^/.]+)')
    def por_categoria(self, request, categoria_id=None):
        posts = Post.objects.filter(categoria__id=categoria_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class ComentariosViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    # GET /comentarios/por-post/<post_id>/
    @action(detail=False, methods=['get'], url_path='por-post/(?P<post_id>[^/.]+)')
    def por_post(self, request, post_id=None):
        comentarios = Comentario.objects.filter(post__id=post_id)
        serializer = self.get_serializer(comentarios, many=True)
        return Response(serializer.data)