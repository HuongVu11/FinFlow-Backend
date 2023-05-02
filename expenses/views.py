from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Sum
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print('GET REQUEST USER ID', request.user.id)
        expenses = Expense.objects.filter(user=request.user.id)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        print('POST REQUEST USER', request.user)
        data['user'] = request.user.id
        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            expense = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseViewID(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        print('PK', pk)
        expense = Expense.objects.get(pk=pk, user=request.user)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = Expense.objects.get(pk=pk, user=request.user)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = Expense.objects.get(pk=pk, user=request.user)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExpenseTotalView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        totalExpenses = Expense.objects.values('category').annotate(totalAmount=Sum('amount')).order_by('-totalAmount').filter(totalAmount__gt=0)
        print('total expense by category: ',totalExpenses)
        return Response(totalExpenses)
