# user/models.py

import os
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import default_storage

# Caminho personalizado para upload das fotos
def user_profile_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"user_{instance.user.id}.{ext}"
    return f"profile_pictures/{filename}"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    foto = models.ImageField(upload_to=user_profile_picture_path, default='profile_pictures/default.jpg')
    descricao = models.TextField(blank=True, default="")

    def save(self, *args, **kwargs):
        # Checa se a foto foi alterada
        try:
            old_instance = Profile.objects.get(pk=self.pk)
            old_foto = old_instance.foto
        except Profile.DoesNotExist:
            old_foto = None

        # Se nova foto for enviada:
        if self.foto and hasattr(self.foto, 'file'):
            try:
                img = Image.open(self.foto)

                if img.format.lower() not in ['jpeg', 'jpg']:
                    raise ValueError("A imagem deve estar no formato JPG.")

                # Converte e comprime
                output = BytesIO()
                img = img.convert('RGB')
                img.save(output, format='JPEG', quality=70)

                # Substitui imagem atual (sem salvar ainda)
                self.foto.save(
                    os.path.basename(self.foto.name),
                    ContentFile(output.getvalue()),
                    save=False
                )

                # Remove imagem anterior se não for a padrão
                if old_foto and old_foto.name != 'profile_pictures/default.jpg' and old_foto != self.foto:
                    if default_storage.exists(old_foto.name):
                        default_storage.delete(old_foto.name)

            except Exception as e:
                print(f"Erro ao processar imagem: {e}")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Perfil de {self.user.username}"
