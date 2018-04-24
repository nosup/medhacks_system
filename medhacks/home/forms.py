from django import forms
from home.models import Application
from django.forms.widgets import SelectDateWidget

class HomeForm(forms.ModelForm):
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
    university = forms.CharField(label='University', max_length=100)
    # forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    graduating_class = forms.IntegerField(label='Graduating Class', max_value=2050)
    major = forms.CharField(label='Major', max_length=50)
    reimbursement = forms.ChoiceField(label='Will you be seeking a travel reimbursement?', choices=(('1', 'No'),('2', 'Yes')))
    essay1 = forms.CharField(label='Why do you want to attend MedHacks 2018? (Max 300 characters)', widget=forms.Textarea)
    essay2 = forms.CharField(label='What skills can you bring to the hackathon? (Max 200 characters)', widget=forms.Textarea)
    essay3 = forms.CharField(label='What would you like to see at MedHacks 2018? (Max 400 characters)', widget=forms.Textarea)
    essay4 = forms.CharField(label='Is there anything you would like us to know? (Max 200 characters)', widget=forms.Textarea)

    class Meta:
        fields = ('first_name', 'last_name', 'email', 'phone_number',
        'address1', 'address2', 'zipcode', 'city', 'country', 'gender',
        'university', 'graduating_class', 'major', 'reimbursement',
        )
        model = Application
