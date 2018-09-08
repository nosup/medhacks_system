from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class RTApp(models.Model):
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
    'The pirates','HTNhelp','E-connect','Neurons','Midnight Mavericks','Bandwidth','Full Source',
    'Glove On','Stimtooth','Scribr','Uprising','E.P.I.C','Klear','JERS','Parachi','Spaghetti','TEAM-NAME?',
    'Groceries','Melanotix','Scarlet Screw','5 Timmies','Medplex','Fugal']
    CHOICES_TEAMS = list(zip(teams, teams))

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
