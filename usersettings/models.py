from django.db import models
from authentications.models import User
from datetime import date

# Create your models here.

class Usersetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=50, default='USD')
    thousand_separator = models.CharField(max_length=50, default='decimal comma (,)')