from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
        model = User

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_password(self):
        data = self.cleaned_data
        if (len(data['password1']) < 8):
            self.fields['password1'].error_messages["error1"] = "Password must contain at least 8 characters"
            raise forms.ValidationError(self.fields['password1'].error_messages["error1"])
        return data['password']
        if (data['password1'] != data['password2']):
            self.fields['password2'].error_messages["error2"] = "Passwords must match"
            raise forms.ValidationError(self.fields['password2'].error_messages["error2"])

    def clean_first_name(self):
        if self.cleaned_data["first_name"].strip() == '':
            self.fields['first_name'].error_messages["error3"] = "First name is required"
            raise forms.ValidationError(self.fields['first_name'].error_messages["error3"])
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if self.cleaned_data["last_name"].strip() == '':
            self.fields['last_name'].error_messages["error4"] = "Last name is required"
            raise forms.ValidationError(self.fields['last_name'].error_messages["error4"])
        return self.cleaned_data["last_name"]

# class EditProfileForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = (
#             'email',
#             'first_name',
#             'last_name',
#             'password'
#         )
#         # exclude = ()
