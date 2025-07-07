# user/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserDetailSerializer
from django.shortcuts import get_object_or_404

User = get_user_model()

class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        user = self._get_user(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = self._get_user(pk)
        if user != request.user:
            return Response({"error": "Você só pode editar seu próprio perfil."}, status=403)

        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        user = self._get_user(pk)
        if user != request.user:
            return Response({"error": "Você só pode excluir sua própria conta."}, status=403)

        user.delete()
        return Response({"message": "Usuário excluído com sucesso."}, status=status.HTTP_204_NO_CONTENT)

    def _get_user(self, identifier):
        try:
            return User.objects.get(username=identifier)
        except User.DoesNotExist:
            return get_object_or_404(User, pk=identifier)
