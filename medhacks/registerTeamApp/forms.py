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
    teams = ['Core 4','IDrops','The Frazzled Five','ZZG','Its Like NLP... But For Team Names',
    'Snowballerz','Doctoc','Five Factorial','Will code for food','Beans in a Can','We Hax','Aviral',
    'QStroke','Dr.Gram','The Fellas','MedShield','Something Too Edgy','The Fellas 2.0','JK','InfoMed',
    'Sick Day Forecast','Safety fit','Davdon','Charcom','JEL','Cas9','Big Brains','BeMetal','QuickFix`',
    'Noti-Fall','LAMA TECH','Dkim','Team Champs','Lucky Penny','Team Slogs','Physia','Team Awesome Sauce',
    'Prometheus','iBioBroskis','High five','Genius Bar','Sandwich','Midwest is Best','Crypto Card','S(Team)D',
    'Citizen Scientist','Yellow Yackets','OTC','Michigan','UniOne','AYA','Qcumber','Featherfall ','Team Number 1',
    'Humpty Dumpties ','Mira','Deacons','AI Socrates ','NutriDoc','TackTile','UR IN LIFE','Tumor Detectives ',
    'Blank','Scrubs','Rehabilita ','No More Headaches','ICU On The Map','Team Johnny','Byte Me','iBioMed',
    'HealthOverall','Spiro','Purple South African Flying Chinchillas','The Rices',
    'The pirates','HTNhelp','E-connect','Neurons','Midnight Mavericks','Bandwidth','Flow Source','EMS Now',
    'Glove On','Stimtooth','Scribr','Uprising','E.P.I.C','Klear','JERS','Parachi','Spaghetti','TEAM-NAME?',
    'Groceries','Melanotix','Scarlet Screw','5 Timmies','Medplex','Fugal','TBD','Just Pick Something','MedCircle','KALE','BaLITmore',
    'WikiMed','Scribbz']
    teams.sort()
    CHOICES_TEAMS = list(zip(teams, teams))

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
