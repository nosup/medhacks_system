from django.db import models
from django.contrib.auth.models import User
from .formatChecker import ContentTypeRestrictedFileField
#from django.core.validators import FileExtensionValidator

# Create your models here.
class Application(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    university = models.CharField(max_length=100, blank=True)
    #university = models.ChoiceField()
    graduating_class = models.IntegerField(blank=True)
    major = models.CharField(max_length=50, blank=True)
    track = models.CharField(max_length=50, blank=True)
    reimbursement = models.CharField(max_length=50, blank=True)
    contingency = models.CharField(max_length=50, blank=True)
    team = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    #resume = models.FileField(upload_to='resume', default='nothing', blank=False)
    resume = ContentTypeRestrictedFileField(upload_to='resume', content_types=['application/pdf','image/jpeg', 'application/docx'],max_upload_size=5242880,blank=False, null=False)
    #resume = models.FileField(upload_to='resume', blank=False, validators=[FileExtensionValidator(['pdf', 'docx', 'jpg'])])
