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
    teams = ['A. I. Socrates for Orthopaedic Education', 'Ambient', 'AMY, the medical assistant', 'AquaMap', 'Arthritis Aid', 'Bandwidth',
    'Bringing Queer Data to the Marketplace', 'CardiaVox', 'CARE', 'CareFall', 'Caring for Caregivers', 'Child Champs', 'Citizen Scientist',
    'CloseCare', 'Concussion detection', 'Crypto Nexus', 'DisAppter', 'Doctoc', 'Donor Book', 'Dr. Gram', 'EEG Simulator', 'Food Alert',
    'FoodPrint', 'FoodShare.me', 'Fugal', 'GloveON!', 'headER', 'Health E-Connect', 'HealthHive', 'iFitness', 'InfoMed', 'InforMED',
    'internal journal', 'iTake', 'LeviChair', 'LBB', 'Lula', 'Lumisoap', 'MakeTheLeap', 'MeChat', 'EZ-EMT', 'zzg', 'Medplex', 'Meds2You',
    'Melanotix', 'Meno BOT', 'Mental Moments', 'Mind Watch', 'MinuteMed', 'MIRA', 'MirageMap', 'MIRROR App', 'MoCli', 'my.Doctor',
    'MyHealth Allies', 'Nearby Nutrition', 'Noti-Fall', 'nurture', 'NutriDoc', 'NutriLyfe', 'O.D. Guard', 'Patrick_I/O', 'Physia',
    'Piece of Mind', 'PillPix', 'PlacePredicts!', 'Pocket Pills', 'Pronto Perio Probe', 'Pure Palm', 'QR Cross', 'QStroke', 'R(eye)covery',
    'Rehabilita', 'SafelyFit', 'Scribr', 'Share The Love', 'Sick Day Forecast', 'SlowDown!', 'Stay Hydrated', 'Strive', 'SymptoKey', 'TackTile',
    'Texting Patients', 'The Gina Gown', 'The Prometheus Network', 'Translational Medicine:sisu', 'TriTag', 'Uplift', 'ZipFood']
    teams.sort()
    CHOICES_TEAMS = list(zip(teams, teams))

    team_name = forms.ChoiceField(label='Select a team from the drop-down to join', choices=CHOICES_TEAMS)
    class Meta:
        fields = ('team_name',
        )
        model = RTApp

class VotePollForm(forms.ModelForm):
    teams = [' A. I. Socrates for Orthopaedic Education', ' Ambient', ' AMY, the medical assistant', ' AquaMap', ' Arthritis Aid', ' Bandwidth',
    ' Bringing Queer Data to the Marketplace', ' CardiaVox', ' CARE', ' CareFall', ' Caring for Caregivers', ' Child Champs', ' Citizen Scientist',
    ' CloseCare', ' Concussion detection', ' Crypto Nexus', ' DisAppter', ' Doctoc', ' Donor Book', ' Dr. Gram', ' EEG Simulator', ' Food Alert',
    ' FoodPrint', ' FoodShare.me', ' Fugal', ' GloveON!', ' headER', ' Health E-Connect', ' HealthHive', ' iFitness', ' InfoMed', ' InforMED',
    ' internal journal', ' iTake', ' LeviChair', 'LBB', ' Lula', ' Lumisoap', ' MakeTheLeap', ' MeChat', ' EZ-EMT', ' zzg', ' Medplex', ' Meds2You',
    ' Melanotix', ' Meno BOT', ' Mental Moments', ' Mind Watch', ' MinuteMed', ' MIRA', ' MirageMap', ' MIRROR App', ' MoCli', ' my.Doctor',
    ' MyHealth Allies', ' Nearby Nutrition', ' Noti-Fall', ' nurture', ' NutriDoc', ' NutriLyfe', ' O.D. Guard', ' Patrick_I/O', ' Physia',
    ' Piece of Mind', ' PillPix', ' PlacePredicts!', ' Pocket Pills', ' Pronto Perio Probe', ' Pure Palm', ' QR Cross', ' QStroke', ' R(eye)covery',
    ' Rehabilita', ' SafelyFit', ' Scribr', ' Share The Love', ' Sick Day Forecast', ' SlowDown!', ' Stay Hydrated', ' Strive', ' SymptoKey', ' TackTile',
    ' Texting Patients', ' The Gina Gown', ' The Prometheus Network', ' Translational Medicine:sisu', ' TriTag', ' Uplift', ' ZipFood']
    teams.sort()
    CHOICES_TEAMS = list(zip(teams, teams))

    choice_field = forms.MultipleChoiceField(choices=CHOICES_TEAMS, widget=forms.CheckboxSelectMultiple)

    class Meta:
        fields = ('choice_field',
        )
        model = PollApp
