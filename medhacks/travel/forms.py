from django import forms
from .models import TRApplication
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.conf import settings
from accounts.models import UserProfile
import json, os, csv, pickle

from django.contrib.admin.widgets import AdminDateWidget

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

    CHOICES_TRAVEL=[('R', Regional),]

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

    permanent_address1 = forms.CharField(label="Address Line 1", max_length=100)
    permanent_address2 = forms.CharField(label="Address Line 2", max_length=100, required=False)
    permanent_city = forms.CharField(label="City", max_length=50)
    permanent_state = forms.ChoiceField(label='State', choices=tupled_list_states)
    permanent_zip = forms.CharField(label="Zip", max_length=15)


    travel_date_from = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
    travel_date_to = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
    travel_location_city = forms.CharField(label="What city are you departing from?", max_length=50)
    travel_location_state = forms.ChoiceField(label='What state are you departing from?', choices=tupled_list_states)
    receipt_amount = forms.DecimalField(max_digits=6, decimal_places=2)
    reimburse_amount = forms.DecimalField(max_digits=6, decimal_places=2)
    receipt_file = forms.FileField(label='Upload Receipt', widget = forms.FileInput, required=True)
    policy_check = forms.BooleanField(label="I have read the <a href='https://drive.google.com/open?id=1IRAy-KqUC7yyR0I8wi7oJ1IxWBkLKIlp'>Receipt Guidelines for Reimbursements</a> and understand that if my information is incorrect or not submitted properly, I will not eligible for a reimbursement.")


    def clean(self):
        cd = self.cleaned_data
        if cd.get('receipt_amount') < cd.get('reimburse_amount'):
            self.add_error('reimburse_amount', "Reimbursement amount cannot be larger than the receipt amount!")
        return cd


    class Meta:
        fields  = ('permanent_address1', 'permanent_address2', 'permanent_city', 'permanent_state', 'permanent_zip', 'travel_date_from', 'travel_date_to',
        'travel_location_city', 'travel_location_state', 'receipt_amount', 'reimburse_amount', 'receipt_file', 'policy_check')
        model = TRApplication
