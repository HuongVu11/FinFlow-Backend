from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions
from .models import Usersetting
from .serializers import UsersettingSerializer
from rest_framework.response import Response

class UsersettingView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print('GET REQUEST USER ID', request.user.id)
        usersettings = Usersetting.objects.filter(user=request.user.id)
        serializer = UserSerializer(usersettings, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        print('POST REQUEST USER', request.user)
        data['user'] = request.user.id
        serializer = Userserializer(data=data)
        if serializer.is_valid():
            Usersetting = serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

class UsersettingViewID(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        print('PK', pk)
        usersetting = Usersetting.objects.get(pk=pk, user=request.user)
        serializer = UsersettingSerializer(usersetting)
        return Response(serializer.data)

    def put(self, request, pk):
        usersetting = Usersetting.objects.get(pk=pk, user=request.user)
        serializer = UsersettingSerializer(usersetting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        usersetting = Usersetting.objects.get(pk=pk, user=request.user)
        usersetting.delete()
        return Response({'message': 'delete'})

