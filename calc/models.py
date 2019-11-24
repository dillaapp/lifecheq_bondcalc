from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Bondinfo(models.Model):
    Title = models.CharField(max_length=200)
    House_price = models.FloatField()
    Deposit = models.IntegerField()
    Interest_rate = models.FloatField()
    Loan_term = models.IntegerField()
    Monthly_payment = models.FloatField()
    Total_interest = models.FloatField()
    Minimum_monthly_income_required = models.FloatField()
    Total_onceoff_payment = models.FloatField()
    Created_at = models.DateTimeField(default=datetime.now, blank=True)
   
    def __str__(self):
      return self.Title