from django.db import models
from authentications.models import User

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

