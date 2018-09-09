from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class RTApp(models.Model):
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

    team_name = models.CharField(max_length=100, default='-', blank=True, null=True, choices=CHOICES_TEAMS)
    users = models.ManyToManyField(User)
    votes = models.IntegerField(default=1, blank=True, null=True)
    def get_users(self):
        users = []
        users = User.objects.filter(userprofile__team_name=self.team_name)
        return ", ".join([u.username for u in users])

# Create your models here.
class PollApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    choice_field = models.CharField(max_length=1000, default='-', blank=True, null=True)
