from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Sum
from .models import Income
from .serializers import IncomeSerializer

class IncomeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print('GET REQUEST USER ID', request.user.id)
        incomes = Income.objects.filter(user=request.user.id)
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        print('POST REQUEST USER', request.user)
        data['user'] = request.user.id
        serializer = IncomeSerializer(data=data)
        if serializer.is_valid():
            income = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncomeViewID(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        print('PK', pk)
        income = Income.objects.get(pk=pk, user=request.user)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)

    def put(self, request, pk):
        income = Income.objects.get(pk=pk, user=request.user)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        income = Income.objects.get(pk=pk, user=request.user)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IncomeTotalView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        totalIncomes = Income.objects.values('category').annotate(total_incomes=Sum('amount')).order_by('-total_incomes').filter(total_incomes__gt=0)
        serializer = IncomeSerializer(totalIncomes, many=True)
        return Response(serializer.data)