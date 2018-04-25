from django import forms
from home.models import Application
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
import json
from django.conf import settings
import os
import ast
class HomeForm(forms.ModelForm):
    #json_data = open('colleges.json').read()
    # STATIC_URL = '/static/'
    #
    # json_data = os.path.join(STATIC_URL, 'colleges.json')
    # data = open(json_data,'r')

    path = os.path.join( settings.STATIC_ROOT, 'colleges.json')
    #print(path)

    f = open(path)
    json_string = f.read()

    counter = 1
    inst = "institution"
    for line in json_string.split('\n'):
        if inst in line:
            counter = counter + 1

    json_data = []
    with open(path) as json_file:
        json_data = json.load(json_file)


    #print(collegeList)


    collegeList = list(json_data)

    #numberList = list(range(1, counter))
    numberList = collegeList
    tupledList = list(zip(numberList,collegeList))
    #collegeList =
    #print(collegeList)

    f.close()


    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    address1 = forms.CharField(label="Address line 1", max_length=50)
    address2 = forms.CharField(label="Address line 2", max_length=50, required=False)
    zipcode = forms.CharField(label="Zipcode", max_length=50, required=False)
    city = forms.CharField(label="City", max_length=50)
    country = forms.CharField(label="Country", max_length=50)
    gender = forms.ChoiceField(label='Gender', choices = (('M', 'Male'), ('F', 'Female')))
    university = forms.ChoiceField(label='University', choices=tupledList)
    # forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    graduating_class = forms.IntegerField(label='Graduating Class', max_value=2050)
    major = forms.CharField(label='Major', max_length=50)
    reimbursement = forms.ChoiceField(label='Will you be seeking a travel reimbursement?', choices=(('No', 'No'),('Yes', 'Yes')))
    essay1 = forms.CharField(label='Why do you want to attend MedHacks 2018? (Max 300 characters)', widget=forms.Textarea)
    essay2 = forms.CharField(label='What skills can you bring to the hackathon? (Max 200 characters)', widget=forms.Textarea)
    essay3 = forms.CharField(label='What would you like to see at MedHacks 2018? (Max 400 characters)', widget=forms.Textarea)
    essay4 = forms.CharField(label='Is there anything you would like us to know? (Max 200 characters)', widget=forms.Textarea)
    resume = forms.FileField(label='Upload Resume', widget = forms.FileInput, required=True)

    class Meta:
        fields = ('first_name', 'last_name', 'email', 'phone_number',
        'address1', 'address2', 'zipcode', 'city', 'country', 'gender',
        'university', 'graduating_class', 'major', 'reimbursement',
        'essay1', 'essay2', 'essay3', 'essay4', 'resume',
        )
        model = Application
    # def __init__(self, *args, **kwargs):
    #     super(HomeForm, self).__init__(*args, **kwargs)
    #     if self.instance:
    #         self.fields['university'].choices = ('1', 'track')
