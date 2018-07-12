from django import forms
from .models import TRApplication
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.conf import settings
from accounts.models import UserProfile
import json, os, csv, pickle

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
    Regional = """ Regional"""
    Midwest = """ Midwest"""
    West = """ West"""
    International = """ International"""

    CHOICES_TRAVEL=[('R', Regional), ('MW', Midwest), ('W', West), ('I', International)]

    CHOICES_YN = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    # TODO Need question in the html
    type_reim = forms.ChoiceField(label='What type of travel reimbursement are you seeking?', choices=CHOICES_TRAVEL, widget=forms.RadioSelect())
    city = forms.CharField(label="City", max_length=50)
    state = forms.ChoiceField(label='State', choices=tupled_list_states)
    country = forms.CharField(label="Country", max_length=50)

    tr_essay = forms.CharField(label='We have a limited number of travel reimbursements. Why should we particularly choose you? (Max 300 characters)', widget=forms.Textarea)
    contingency = forms.ChoiceField(label='Is your attendance to MedHacks 2018 contingent on receiving a travel reimbursement?', choices=CHOICES_YN, widget=forms.RadioSelect())


    class Meta:
        fields = ('type_reim', 'city', 'state', 'country', 'tr_essay', 'contingency',
        )
        model = TRApplication

class TravelReceiptForm(forms.ModelForm):
    path_to_states = os.path.join(settings.STATIC_ROOT, 'states.pickle')
    with open(path_to_states, 'rb') as handle:
        tupled_list_states = pickle.load(handle)

    travel_date_from = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
    travel_date_to = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
    travel_location_city = forms.CharField(label="City", max_length=50)
    travel_location_state = forms.ChoiceField(label='State', choices=tupled_list_states)
    receipt_amount = forms.IntegerField()
    reimburse_amount = forms.IntegerField()

    class Meta:
        fields  = ('travel_date_from', 'travel_date_to', 'travel_location_city',
        'travel_location_state', 'receipt_amount', 'reimburse_amount',)
        model = TRApplication

    class Meta:
        fields = ('receipt_amount',)
        model = UserProfile
