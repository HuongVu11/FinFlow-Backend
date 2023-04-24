from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from authentications.views import UserRegisterView, UserLoginView, UserLogoutView
from authentications.views import AuthenticationViewSet
from incomes.views import IncomeViewSet

# create a new router
router = routers.DefaultRouter()
# register the viewsets
router.register(r'incomes', IncomeViewSet, basename='income')
router.register(r'authentications', AuthenticationViewSet, basename='authentication')

urlpatterns = [
    path('', include(router.urls)),
    # path('users/register/', UserRegisterView.as_view()),
    # path('users/login/', UserLoginView.as_view()),
    # path('users/logout/', UserLogoutView.as_view()),
    path('admin/', admin.site.urls),
]
