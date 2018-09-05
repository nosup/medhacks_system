from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class RTApp(models.Model):
    team_name = models.CharField(max_length=100, default='-', blank=True, null=True)
    # team_join = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
