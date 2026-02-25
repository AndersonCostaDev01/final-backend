from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Post, Categoria, Comentario
from .serializers import (
    PostSerializer,
    CategoriaSerializer,
    ComentarioSerializer
)


# =========================
# CATEGORIAS
# =========================
class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# =========================
# POSTS
# =========================
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    queryset = Post.objects.all().select_related(
        'autor',
        'categoria'
    ).prefetch_related(
        'likes',
        'comentarios'
    )

    # Autor vem SEMPRE do token
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    # GET /posts/por-categoria/<categoria_id>/
    @action(
        detail=False,
        methods=['get'],
        url_path='por-categoria/(?P<categoria_id>[^/.]+)'
    )
    def por_categoria(self, request, categoria_id=None):
        posts = self.queryset.filter(categoria__id=categoria_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    # POST /posts/<id>/like/
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated]
    )
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True

        return Response({
            "liked": liked,
            "total_likes": post.likes.count()
        })


# =========================
# COMENTÁRIOS
# =========================
class ComentariosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ComentarioSerializer

    queryset = Comentario.objects.all().select_related(
        'autor',
        'post'
    )

    # Autor do comentário vem do token
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    # GET /comentarios/por-post/<post_id>/
    @action(
        detail=False,
        methods=['get'],
        url_path='por-post/(?P<post_id>[^/.]+)'
    )
    def por_post(self, request, post_id=None):
        comentarios = self.queryset.filter(post__id=post_id)
        serializer = self.get_serializer(comentarios, many=True)
        return Response(serializer.data)