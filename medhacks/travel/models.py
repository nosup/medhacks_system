from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .formatcheck import ContentTypeRestrictedFileField
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
    type_reim = models.CharField(max_length=5, default = '-')
    # below starts the travel receipts
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Permanent Address
    travel_date_from = models.DateTimeField(blank=True, null=True)
    travel_date_to = models.DateTimeField(blank=True, null=True)
    travel_location_city = models.CharField(max_length=50)
    travel_location_state = models.CharField(max_length=50, default = 'NA')
    receipt_amount = models.IntegerField(default = 0)
    reimburse_amount = models.IntegerField(default = 0)
    receipt_file = ContentTypeRestrictedFileField(upload_to='receipts', content_types=['application/pdf','application/docx','application/vnd.openxmlformats-officedocument.wordprocessingml.document','application/doc','image/jpeg'],max_upload_size=2097152,blank=False, null=False)
    # radio: I accept that if wrong submission, no reimbursement
