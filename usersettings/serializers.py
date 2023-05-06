from rest_framework import serializers
from .models import Usersetting

class UsersettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersetting
        fields = '__all__'