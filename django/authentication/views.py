from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

import jwt
from .serializers import UserSerializer, LoginSerializer

# Create your views here.
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer_class = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.request.method == 'POST':
            return []
        return super().get_permissions()

    def post(self, request):
        serializer_class = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
