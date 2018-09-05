from django import forms
from .models import RTApp
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.conf import settings
from accounts.models import UserProfile
import json, os, csv, pickle

from django.contrib.admin.widgets import AdminDateWidget

class CreateTeamRegisterForm(forms.ModelForm):

    team_name = forms.CharField(label="team_name", max_length=50)

    class Meta:
        fields = ('team_name',
        )
        model = RTApp

class SelectTeamForm(forms.ModelForm):

    #team_join = forms.ModelChoiceField(queryset=RTApp.objects.all())
    team_join = forms.ModelChoiceField(queryset=RTApp.objects.all().values_list('team_name', flat=True))
                                        #queryset=Books.objects.all().order_by('name')
    #team_join = forms.ChoiceField(label='Gender', choices = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('Prefer not to say', 'Prefer not to say')))
    class Meta:
        fields = ('team_join',
        )
        model = RTApp
