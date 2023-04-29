from django.db import models
from authentications.models import User
from datetime import date

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('housing', 'Housing'),
        ('transportation', 'Transportation'),
        ('entertainment', 'Entertainment'),
        ('personal care', 'Personal Care'),
        ('health', 'Health'),
        ('education', 'Education'),
        ('kids', 'Kids'),
        ('pets', 'Pets'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    date = models.DateField(default=date.today)