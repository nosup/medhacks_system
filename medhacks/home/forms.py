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

    # get list of states for dropdown
    path_to_states = os.path.join(settings.STATIC_ROOT, 'states.csv')
    with open(path_to_states, 'r', encoding='utf-8') as file:
        states = csv.reader(file)
        states_list = list(states)
    states_list = [a[0] for a in states_list]
    states_list.pop(0)
    states_list.insert(0, 'NA')
    tupled_list_states = list(zip(states_list,states_list))

    CHOICESMEDHACKS=[('Yes',' Yes'), ('No',' No')]
    CHOICES_HEARD = [('Facebook', ' Facebook'), ('Instagram', ' Instagram'), ('MLH', ' MLH'),
    ('Campus Ambassador', ' MedHacks Campus Ambassador'), ('Other', ' Other')]

    first_name = forms.CharField(label='First Name', max_length=50, widget = forms.HiddenInput())
    last_name = forms.CharField(label='Last Name', max_length=50, widget = forms.HiddenInput())
    email = forms.EmailField(label='Email', max_length=50, widget = forms.HiddenInput())
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    city = forms.CharField(label="City", max_length=50)
    state = forms.ChoiceField(label='State', choices=tupled_list_states)
    country = forms.CharField(label="Country", max_length=50)
    gender = forms.ChoiceField(label='Gender', choices = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('Prefer not to say', 'Prefer not to say')))
    education = forms.ChoiceField(label='Current Level of Education', choices =
        (('High School', 'High School'), ('Undergraduate', 'Undergraduate'),
        ('Graduate', 'Graduate'), ('Professional', 'Professional')))
    university = forms.ChoiceField(label='University', choices=tupled_list_colleges)
    other_uni = forms.CharField(label='Other University', max_length=100, required=False)
    # forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    graduating_class = forms.ChoiceField(label='Graduating Class', choices=(('NA','NA'),('2018','2018'), ('2019','2019'), ('2020','2020'), ('2021+','2021+')))
    major = forms.ChoiceField(label='Major/Area of Expertise', choices=tupled_list_majors)
    secondmajor = forms.ChoiceField(label='Second Major/Area of Expertise', choices=tupled_list_majors, required=False)
    attended = forms.ChoiceField(label='Have you attended MedHacks previously?', choices=CHOICESMEDHACKS, widget=forms.RadioSelect())
    reimbursement = forms.ChoiceField(label='Will you be seeking a travel reimbursement?', choices=CHOICESMEDHACKS, widget=forms.RadioSelect())
    essay1 = forms.CharField(label='Why do you want to attend MedHacks 2018? (Max 300 characters)', widget=forms.Textarea)
    essay2 = forms.CharField(label='What skills can you bring to the hackathon? (Max 200 characters)', widget=forms.Textarea)
    essay3 = forms.CharField(label='What would you like to see at MedHacks 2018? (Max 300 characters)', widget=forms.Textarea)
    essay4 = forms.CharField(label='Is there anything you would like us to know? (Max 200 characters)', widget=forms.Textarea, required=False)
    resume = forms.FileField(label='Upload Resume', widget = forms.FileInput, required=True)
    how_heard_medhacks = forms.ChoiceField(label='How did you hear about MedHacks 2018', choices=CHOICES_HEARD, widget=forms.RadioSelect())
    permission = forms.BooleanField(label='I am giving MedHacks use of my personal information',required=True)
    conduct = forms.BooleanField(label='I accept the <a href="https://static.mlh.io/docs/mlh-code-of-conduct.pdf"target="_blank">MLH code of conduct</a>',required=True)
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
        # if self.cleaned_data['permission'] == 'False':
        #     self.add_error('Please checkmark this box')

    class Meta:
        fields = ('first_name', 'last_name', 'email', 'phone_number',
        'city', 'state', 'country', 'gender',
        'education', 'university', 'other_uni', 'major','secondmajor','graduating_class', 'reimbursement', 'attended',
        'essay1', 'essay2', 'essay3', 'essay4','how_heard_medhacks','resume', 'permission', 'conduct',
        )
        model = Application
