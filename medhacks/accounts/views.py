from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import (
    RegistrationForm,
    # EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.models import Application
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def home(request):
    posts = Application.objects.filter(email=request.user.email)[:1]
    args = {'posts': posts}
    return render(request, 'accounts/home.html', args)

def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            sender = settings.DEFAULT_FROM_EMAIL
            recipient = [form.cleaned_data['email']]
            subject = 'MedHacks Account'
            content = render_to_string('accounts/account_created_email.html', {'user':user})
            send_mail(subject,content,sender,recipient,fail_silently=False)
            return redirect(reverse('accounts:home'))
    return render(request, 'accounts/reg_form.html', {'form': form})

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # sender = settings.DEFAULT_FROM_EMAIL
            # recipient = [form.user['email']]
            # subject = 'Change Password'
            # content = render_to_string('accounts/change_password_email.html')
            # send_mail(subject,content,sender,recipient,fail_silently=False)
            return redirect(reverse('accounts:view_profile'))
        else:
            # TODO print error message: "incorrect password entry", etc
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
