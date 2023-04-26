from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from .models import Balance
from .serializers import BalanceSerializer
from authentications.models import User

class BalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        income_total = user.income_set.aggregate(Sum('amount'))['amount__sum'] or 0
        expense_total = user.expense_set.aggregate(Sum('amount'))['amount__sum'] or 0
        balance = income_total - expense_total
        # Save the balance in the database
        balance_object, created = Balance.objects.update_or_create(
            user=request.user,
            defaults={'balance': balance}
        )
        return Response({'balance': balance})