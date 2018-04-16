from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Application(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    graduating_class = models.IntegerField()
    major = models.CharField(max_length=50)
    track = models.CharField(max_length=50)
    reimbursement = models.CharField(max_length=50)
    contingency = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
