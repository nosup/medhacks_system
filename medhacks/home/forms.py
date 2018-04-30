from django import forms
from home.models import Application
from django.forms.widgets import SelectDateWidget
from django.core.exceptions import ValidationError
from django.conf import settings
import json
import os
import csv

class HomeForm(forms.ModelForm):
    path_to_colleges = os.path.join(settings.STATIC_ROOT, 'colleges.json')

    json_data = []

    #need encoding to prevent error on live server
    with open(path_to_colleges, encoding='utf-8') as json_file:
        json_data = json.load(json_file)


    onlyCollegeList = []
    for piece in json_data:
        this_ip = piece['institution']
        onlyCollegeList.append(this_ip)

    #sorted and deletes duplicates from onlyCollegeList
    onlyCollegeList = sorted(set(onlyCollegeList))

    onlyCollegeList.insert(0, 'Other')
    onlyCollegeList.insert(0, 'NA')
    #puts onlyCollegeList into a tupled list of choices for forms
    tupled_list_colleges = list(zip(onlyCollegeList, onlyCollegeList))
    #tupledList = (('1', 'Temp1'), ('2', 'Temp2'))

    path_to_majors = os.path.join(settings.STATIC_ROOT, 'major_list.csv')

    with open(path_to_majors, 'r') as f:
        reader = csv.reader(f)
        complete_majors_list = list(reader)

    only_majors_list = [a[1] for a in complete_majors_list]

    #delete first index of major list because it is not a major(it's a header)
    only_majors_list.pop(0)
    only_majors_list = sorted(only_majors_list)

    majors_lower = [x.lower() for x in only_majors_list]

    for x in range(len(majors_lower)):
        majors_lower[x] = majors_lower[x].title()
        x = x + 1

    majors_lower.insert(0, 'Other')
    majors_lower.insert(0, 'NA')

    tupled_list_majors = list(zip(majors_lower, majors_lower))
    #print(only_majors_list)
    CHOICESMEDHACKS=[('Yes','Yes'), ('No','No')]

    first_name = forms.CharField(label='First Name', max_length=50, widget = forms.HiddenInput())
    last_name = forms.CharField(label='Last Name', max_length=50, widget = forms.HiddenInput())
    email = forms.EmailField(label='Email', max_length=50, widget = forms.HiddenInput())
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    address1 = forms.CharField(label="Address line 1", max_length=50)
    address2 = forms.CharField(label="Address line 2", max_length=50, required=False)
    zipcode = forms.CharField(label="Zipcode", max_length=50, required=False)
    city = forms.CharField(label="City", max_length=50)
    country = forms.CharField(label="Country", max_length=50)
    gender = forms.ChoiceField(label='Gender', choices = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('Prefer not to say', 'Prefer not to say')))
    education = forms.ChoiceField(label='Current Level of Education', choices =
        (('High School', 'High School'), ('Undergraduate', 'Undergraduate'),
        ('Graduate', 'Graduate'), ('Professional', 'Professional')))
    university = forms.ChoiceField(label='University', choices=tupled_list_colleges)
    other_uni = forms.CharField(label='Other University', max_length=100, required=False)
    # forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    graduating_class = forms.IntegerField(label='Graduating Class', max_value=2050)
    major = forms.ChoiceField(label='Major', choices=tupled_list_majors)
    secondmajor = forms.ChoiceField(label='Second Major', choices=tupled_list_majors, required=False)
    attended = forms.ChoiceField(label='Have you attended MedHacks previously?', choices=CHOICESMEDHACKS, widget=forms.RadioSelect())
    reimbursement = forms.ChoiceField(label='Will you be seeking a travel reimbursement?', choices=CHOICESMEDHACKS, widget=forms.RadioSelect())
    essay1 = forms.CharField(label='Why do you want to attend MedHacks 2018? (Max 300 characters)', widget=forms.Textarea)
    essay2 = forms.CharField(label='What skills can you bring to the hackathon? (Max 200 characters)', widget=forms.Textarea)
    essay3 = forms.CharField(label='What would you like to see at MedHacks 2018? (Max 400 characters)', widget=forms.Textarea)
    essay4 = forms.CharField(label='Is there anything you would like us to know? (Max 200 characters)', widget=forms.Textarea, required=False)
    resume = forms.FileField(label='Upload Resume', widget = forms.FileInput, required=True)

    # def clean_other_uni(self):
    #     if self.cleaned_data['university'] == 'Other' and self.cleaned_data['other_uni'] == '':
    #         self.cleaned_data['other_uni'] = 'None'
    #         raise ValidationError("Please enter your university")
    #     return self.cleaned_data['other_uni']

    def clean(self):
        if self.cleaned_data['university'] == 'Other':
            if self.cleaned_data['other_uni'] == '':
                self.add_error('other_uni', "Please enter your university")
            else:
                self.cleaned_data['university'] = self.cleaned_data['other_uni']

    class Meta:
        fields = ('first_name', 'last_name', 'email', 'phone_number',
        'address1', 'address2', 'zipcode', 'city', 'country', 'gender',
        'education', 'university', 'other_uni', 'major','secondmajor','graduating_class', 'reimbursement', 'attended',
        'essay1', 'essay2', 'essay3', 'essay4', 'resume',
        )
        model = Application
