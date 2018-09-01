from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .formatcheck import ContentTypeRestrictedFileField
from datetime import datetime

# Create your models here.
class RTApp(models.Model):
    team_name = models.CharField(max_length=50)
