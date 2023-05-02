from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentications.views import AuthenticationViewSet
from incomes.views import IncomeView, IncomeViewID, IncomeTotalView
from expenses.views import ExpenseView, ExpenseViewID, ExpenseTotalView
from balances.views import BalanceView

# create a new router
router = routers.DefaultRouter()
# register the viewsets
router.register(r'authentications', AuthenticationViewSet, basename='authentication')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('incomes/', IncomeView.as_view()),
    path('incomes/<int:pk>/', IncomeViewID.as_view()),
    path('incomes/total/', IncomeTotalView.as_view()),
    path('expenses/', ExpenseView.as_view()),
    path('expenses/<int:pk>/', ExpenseViewID.as_view()),
    path('expenses/total/', ExpenseTotalView.as_view()),
    path('balance/', BalanceView.as_view())
]
