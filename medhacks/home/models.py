from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .formatChecker import ContentTypeRestrictedFileField
# Create your models here.
class Application(models.Model):
    first_name = models.CharField(max_length=50, default='-')
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    # address1 = models.CharField(max_length=50)
    # address2 = models.CharField(max_length=50)
    # zipcode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default = 'NA')
    gender = models.CharField(max_length=50)
    education = models.CharField(max_length=20, default = '-')
    university = models.CharField(max_length=100)
    graduating_class = models.CharField(max_length=50, default='NA')
    major = models.CharField(max_length=50)
    secondmajor = models.CharField(max_length=50, default = 'NA')
    essay1 = models.CharField(max_length=300, default = '-')
    essay2 = models.CharField(max_length=300, default = '-')
    essay3 = models.CharField(max_length=300, default = '-')
    essay4 = models.CharField(max_length=300, default = '-')
    reimbursement = models.CharField(max_length=50)
    attended = models.CharField(max_length=50, default = 'No')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = ContentTypeRestrictedFileField(upload_to='resume', content_types=['application/pdf','application/docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document','application/doc','image/jpeg'],max_upload_size=2097152,blank=False, null=False)
