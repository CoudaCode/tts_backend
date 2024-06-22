from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializer import *
from django.http import JsonResponse

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfilUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializerProfile(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



class UserProfileView(generics.RetrieveAPIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            user_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                # Ajoutez d'autres champs que vous souhaitez exposer
            }
            return JsonResponse(user_data, status=200)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)