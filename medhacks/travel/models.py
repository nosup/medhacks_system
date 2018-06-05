from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class TRApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default = 'NA')
    country = models.CharField(max_length=50)
    tr_essay = models.CharField(max_length=300, default = '-')
    contingency = models.CharField(max_length=5)
    submit_time = models.DateTimeField(auto_now_add=True)
