from django import forms
from .models import RTApp
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.conf import settings
from accounts.models import UserProfile
import json, os, csv, pickle

from django.contrib.admin.widgets import AdminDateWidget

class CreateTeamRegisterForm(forms.ModelForm):

    team_name = forms.CharField(label="team_name", max_length=100)

    class Meta:
        fields = ('team_name',
        )
        model = RTApp

class SelectTeamForm(forms.ModelForm):
    CHOICES_TEAMS = (
        ('-', 'None'),
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
    )

    team_name = forms.ChoiceField(choices=CHOICES_TEAMS)
    class Meta:
        fields = ('team_name',
        )
        model = RTApp
