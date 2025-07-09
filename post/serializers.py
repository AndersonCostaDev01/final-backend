from rest_framework import serializers
from .models import Post, Categoria, Comentario
from user.models import CustomUser


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(source='autor.username', read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'autor', 'autor_username', 'conteudo', 'data_comentario', 'post']


class PostSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(source='autor.username', read_only=True)
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    total_likes = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'titulo', 'conteudo', 'data_publicacao',
            'autor', 'autor_username', 'categoria', 'categoria_nome',
            'likes', 'total_likes', 'comentarios'
        ]
