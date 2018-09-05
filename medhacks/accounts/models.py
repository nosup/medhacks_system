from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from registerTeamApp.models import RTApp
# Create your models here.

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset()
        # .filter(city='London')

class UserProfile(models.Model):
    # Generic Y/N choices
    CHOICES_YN = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('-', 'Not Decided'),
    )

    # For Travel Reimbursement Specific Choices
    CHOICES_TR = (
        ('-', 'Not Decided'),
        ('Rejected', 'Rejected'),
        ('Regional', 'Regional'),
        ('Midwest', 'Midwest'),
        ('West', 'West'),
        ('International', 'International'),
    )

    # For teams_choices
    CHOICES_TEAMS = (
        ('-', 'None'),
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
    )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # description = models.CharField(max_length=100, default='')
    # city = models.CharField(max_length=100, default='')
    # website = models.URLField(default='')
    # phone = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    travel_reimbursement = models.CharField(max_length=13, choices=CHOICES_TR, default='-')
    travel_confirm = models.CharField(max_length=1, choices=CHOICES_YN, default='-')
    receipt_amount = models.IntegerField(default=0)
    campus_ambassador = models.CharField(max_length=1, choices=CHOICES_YN, default='-')
    accepted = models.CharField(max_length=1, choices=CHOICES_YN, default='-')
    confirmation = models.CharField(max_length=1, choices=CHOICES_YN, default='-')
    team_name = models.CharField(max_length=100, default='-')

    # image = models.ImageField(upload_to='profile_image', blank=True)

    # london = UserProfileManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
