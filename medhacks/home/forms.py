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
    #print(json_string)
    json_string = json_string.replace('[', '(')
    json_string = json_string.replace(']', ')')
    json_string = json_string.replace('{', '(')
    json_string = json_string.replace('}', ')')
    json_string = json_string.replace(':', ',')

    #print(json_string)
    counter = 1
    collegechoices = ""

    inst = "institution"
    for line in json_string.split('\n'):
        if inst in line:
            line = line.replace(inst, str(counter))
            line = '(' + line + '),'
            collegechoices = collegechoices + line
            #print(line)
            counter = counter + 1
    collegechoices = '(' + collegechoices + ')'
    tuplecollegechoices = tuple(collegechoices,)
    #print(tuple(collegechoices,))
    #print(collegechoices)
    #json_object = json.load(f)

    json_data = []
    with open(path) as json_file:
        json_data = json.load(json_file)

    collegeList = list(json_data)

    #print(collegeList)


    #print(collegeList)
    numberList = list(range(1, counter))
    tupledList = list(zip(numberList,collegeList))
    tupledList = [item.replace("'", "") for item in tupledList]

    #collegeList =
    #print(collegeList)

    f.close()


    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    phone_number = forms.CharField(label='Phone Number')
    address1 = forms.CharField(label="Address line 1", max_length=50)
    address2 = forms.CharField(label="Address line 2", max_length=50, required=False)
    zipcode = forms.CharField(label="Zipcode", max_length=50, required=False)
    city = forms.CharField(label="City", max_length=50)
    country = forms.CharField(label="Country", max_length=50)
    gender = forms.ChoiceField(label='Gender', choices = (('M', 'Male'), ('F', 'Female')))
    #university = forms.CharField(label='University', max_length=100)
    university = forms.ChoiceField(label='University', choices=tupledList)
    graduating_class = forms.IntegerField(label='Graduating Class', max_value=2050)
    major = forms.CharField(label='Major', max_length=50)
    track = forms.ChoiceField(label='Track', choices=(('1', 'Track1'),('2', 'Track2'),('3', 'Track3')))
    reimbursement = forms.ChoiceField(label='Travel Reimbursement', choices=(('1', 'No'),('2', 'Yes')))
    contingency = forms.ChoiceField(label='Contingency', choices=(('1', 'No'),('2', 'Yes')))
    team = forms.ChoiceField(label='Team', choices=(('1', 'No'),('2', 'Yes')))
    resume = forms.FileField(label='Upload Resume', widget = forms.FileInput, required=True)
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'phone_number',
        'address1', 'address2', 'zipcode', 'city', 'country', 'gender',
        'university', 'graduating_class', 'major', 'track', 'reimbursement',
        'contingency', 'team', 'resume')
        model = Application
    # def __init__(self, *args, **kwargs):
    #     super(HomeForm, self).__init__(*args, **kwargs)
    #     if self.instance:
    #         self.fields['university'].choices = ('1', 'track')
