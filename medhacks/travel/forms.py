from django import forms
from .models import TRApplication
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.conf import settings
import json
import os
import csv

class TravelForm(forms.ModelForm):
    # get list of states for dropdown
    path_to_states = os.path.join(settings.STATIC_ROOT, 'states.csv')
    with open(path_to_states, 'r', encoding='utf-8') as file:
        states = csv.reader(file)
        states_list = list(states)
    states_list = [a[0] for a in states_list]
    states_list.pop(0)
    states_list.insert(0, 'NA')
    tupled_list_states = list(zip(states_list,states_list))

    CHOICESMEDHACKS=[('Yes','Yes'), ('No','No')]

    CHOICES_YN = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('-', 'Not Decided'),
    )

    # TODO Need question in the html
    city = forms.CharField(label="City", max_length=50)
    state = forms.ChoiceField(label='State', choices=tupled_list_states)
    country = forms.CharField(label="Country", max_length=50)

    tr_essay = forms.CharField(label='We have a limited number of travel reimbursements. Why should we particularly choose you? (Max 300 characters)', widget=forms.Textarea)
    contingency = forms.ChoiceField(label='Is your attendance to MedHacks 2018 contingent on receiving a travel reimbursement?', choices=CHOICES_YN, widget=forms.RadioSelect())


    class Meta:
        fields = ('city', 'state', 'country', 'tr_essay', 'contingency',
        )
        model = TRApplication
