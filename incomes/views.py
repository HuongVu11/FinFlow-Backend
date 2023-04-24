from .models import Income
from rest_framework import viewsets, permissions
from .serializers import IncomeSerializer
# from django.views.decorators.csrf import csrf_exempt

# class IncomeViewSet(viewsets.ModelViewSet):
#     serializer_class = IncomeSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Income.objects.filter(user=request.user)
    # permission_classes = [permissions.AllowAny]
    # queryset = Income.objects.all()
    # @csrf_exempt
    # def get_queryset(self):
    #     print(self.request.user)
    #     return Income.objects.filter(user=self.request.user)
    
    # def post(self, request):
    #     return Income.objects.create(user=self.request.user)

from rest_framework.decorators import action
from rest_framework.response import Response

class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def all(self, request):
        incomes = self.get_queryset()
        serializer = self.serializer_class(incomes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        income = self.get_object()
        serializer = self.serializer_class(income)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        income = self.get_object()
        serializer = self.serializer_class(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        income = self.get_object()
        income.delete()
        return Response(status=204)
