from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    print(queryset)
    serializer_class = UserSerializer
