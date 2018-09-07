from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class RTApp(models.Model):
    CHOICES_TEAMS = (
        ('-', 'None'),
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
    )
    team_name = models.CharField(max_length=100, default='-', blank=True, null=True, choices=CHOICES_TEAMS)
    users = models.ManyToManyField(User)
    def get_users(self):
        users = []
        users = User.objects.filter(userprofile__team_name=self.team_name)
        return ", ".join([u.username for u in users])

# Create your models here.
class PollApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    choice_field = models.CharField(max_length=1000, default='-', blank=True, null=True)
