from django import forms
from .models import RTApp, PollApp
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
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
    )

    team_name = forms.ChoiceField(label='Select a team from the drop-down to join', choices=CHOICES_TEAMS)
    class Meta:
        fields = ('team_name',
        )
        model = RTApp

class VotePollForm(forms.ModelForm):

    #This is a copy of CHOICES_TEAMS
    SAMPLE_CHOICES = (
        ('-', 'None'),
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
    )
    choice_field = forms.MultipleChoiceField(choices=SAMPLE_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        fields = ('choice_field',
        )
        model = PollApp
