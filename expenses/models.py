from django.db import models
from authentications.models import User
from datetime import date

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('housing', 'Housing'),
        ('transportation', 'Transportation'),
        ('insurance', 'Insurance'),
        ('entertainment', 'Entertainment'),
        ('personal care', 'Personal Care'),
        ('healthcare', 'Healthcare'),
        ('loan', 'Loan'),
        ('taxes', 'Taxes'),
        ('gifts and donations', 'Gifts and Donations'),
        ('savings or investments', 'Savings or Investments'),
        ('kids', 'Kids'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    date = models.DateField(default=date.today)