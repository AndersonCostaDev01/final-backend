from django.db import models
from user.models import CustomUser


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='posts_liked', blank=True)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_comentario']

    def __str__(self):
        return f"Comentário de {self.autor} em {self.post}"
