# user\serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

# Serializador do perfil (foto e bio)
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['foto', 'descricao']

    def validate_foto(self, value):
        if value:
            if not value.name.lower().endswith(('.jpg', '.jpeg')):
                raise serializers.ValidationError("A imagem deve estar no formato JPG.")
        return value

# Registro de novo usuário
class UserRegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=5)
    first_name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'profile']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # NÃO chame user.profile.save() aqui, a menos que você vá alterar algo no perfil
        return user

# Visualização e edição do perfil completo
class UserDetailSerializer(serializers.ModelSerializer):
    foto = serializers.ImageField(source='profile.foto', required=False)
    descricao = serializers.CharField(source='profile.descricao', required=False)

    class Meta:
        model = User
        fields = ['username', 'foto', 'descricao', 'first_name', 'last_name']
        read_only_fields = ['username']

    def update(self, instance, validated_data):
        # Atualiza dados do usuário
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        # Atualiza dados do perfil
        profile_data = validated_data.get('profile', {})
        profile = instance.profile
        profile.foto = profile_data.get('foto', profile.foto)
        profile.descricao = profile_data.get('descricao', profile.descricao)
        profile.save()

        return instance

    def validate_foto(self, value):
        if value and not value.name.lower().endswith(('.jpg', '.jpeg')):
            raise serializers.ValidationError("A imagem deve estar no formato JPG.")
        return value
