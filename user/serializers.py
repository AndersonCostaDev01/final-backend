from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

# Obtém o modelo de usuário padrão do Django
User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile  # Define o modelo Profile para serialização
        fields = ['foto', 'descricao']  # Campos que serão serializados

    def validate_foto(self, value):
        # Validação customizada para garantir que a foto seja JPG
        if value:
            if not value.name.lower().endswith('.jpg') and not value.name.lower().endswith('.jpeg'):
                raise serializers.ValidationError("A imagem deve estar no formato JPG.")
        return value


class UserRegisterSerializer(serializers.ModelSerializer):
    # Define campos personalizados para o serializer
    profile = ProfileSerializer(read_only=True)  # Inclui dados do perfil (somente leitura)
    email = serializers.EmailField(required=True)  # Email obrigatório
    password = serializers.CharField(write_only=True, min_length=5)  # Senha com mínimo 5 caracteres
    first_name = serializers.CharField(max_length=25)  # Nome com máximo 25 caracteres
    last_name = serializers.CharField(max_length=50)  # Sobrenome com máximo 50 caracteres

    class Meta:
        model = User  # Define o modelo User para serialização
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'profile']  # Campos incluídos

    def create(self, validated_data):
        # Método para criar novo usuário
        password = validated_data.pop('password')  # Remove senha dos dados validados
        user = User(**validated_data)  # Cria instância do usuário
        user.set_password(password)  # Define senha criptografada
        user.save()  # Salva usuário
        Profile.objects.create(user=user)  # Cria perfil associado ao usuário
        return user
