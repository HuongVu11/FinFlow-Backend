from .models import Income
from rest_framework import serializers

# class IncomeSerializer(serializers.HyperlinkedModelSerializer):
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id', 'user', 'category', 'name', 'amount', 'date')
