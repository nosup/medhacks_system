from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import (
    RegistrationForm,
    # EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.models import Application

def home(request):
    posts = Application.objects.filter(email=request.user.email)[:1]
    args = {'posts': posts}
    return render(request, 'accounts/home.html', args)

def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    return render(request, 'accounts/reg_form.html', {'form': form})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('accounts:view_profile'))
#     else:
#         form = EditProfileForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            # TODO print error message: "incorrect password entry", etc
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
