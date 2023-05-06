from django.db import models
from authentications.models import User
from datetime import date

# Create your models here.

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    date = models.DateField(default=date.today)