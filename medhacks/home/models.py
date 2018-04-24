from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.
class Application(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    graduating_class = models.IntegerField()
    major = models.CharField(max_length=50)
    essay1 = models.CharField(max_length=300, default = '-')
    essay2 = models.CharField(max_length=300, default = '-')
    essay3 = models.CharField(max_length=300, default = '-')
    essay4 = models.CharField(max_length=300, default = '-')
    # track = models.CharField(max_length=50)
    reimbursement = models.CharField(max_length=50)
    # contingency = models.CharField(max_length=50)
    # team = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
