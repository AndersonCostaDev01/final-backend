from rest_framework import serializers
from .models import Post, Categoria, Comentario


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(
        source='autor.username',
        read_only=True
    )

    class Meta:
        model = Comentario
        fields = [
            'id',
            'autor',
            'autor_username',
            'conteudo',
            'data_comentario',
            'post'
        ]


class PostSerializer(serializers.ModelSerializer):
    autor_username = serializers.CharField(
        source='autor.username',
        read_only=True
    )
    categoria_nome = serializers.CharField(
        source='categoria.nome',
        read_only=True
    )
    comentarios = ComentarioSerializer(
        many=True,
        read_only=True
    )

    total_likes = serializers.SerializerMethodField()
    liked_by_me = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'titulo',
            'conteudo',
            'data_publicacao',
            'autor',
            'autor_username',
            'categoria',
            'categoria_nome',
            'total_likes',
            'liked_by_me',
            'comentarios'
        ]

    def get_total_likes(self, obj):
        return obj.likes.count()

    def get_liked_by_me(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False