from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from .models import User
import json

class AuthenticationViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    # @csrf_exempt
    def register(self, request):
        data = json.loads(request.body.decode('utf-8'))
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            repassword  = data['repassword']
            if not password or not username:
                return Response({'message': 'Please provide all required fields.'}, status=status.HTTP_400_BAD_REQUEST)
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    return Response({'message': 'This username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user = User.objects.create_user(username=username, password=password)
                    login(request, user)
                    return Response({'data': {'id': user.id, 'username': user.username}}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    @csrf_exempt
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'data': {'id': user.id, 'username': user.username}}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    # @csrf_exempt
    def logout(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)
