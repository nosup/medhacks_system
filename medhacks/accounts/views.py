from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.models import Application
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from .forms import ConfirmAcceptanceForm
from .models import UserProfile

def home(request):
    posts = Application.objects.filter(email=request.user.email)[:1]
    args = {'apps': posts}
    return render(request, 'home/home.html', args)

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
            return redirect(reverse('home:home'))
    return render(request, 'accounts/reg_form.html', {'form': form})

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

class ConfirmView(TemplateView):
    template_name = 'accounts/confirm.html'

    def get(self, request):
        form = ConfirmAcceptanceForm
        get_q1 = UserProfile.objects.filter(user=request.user)
        get_acceptance_yes = get_q1.filter(accepted='Y')
        print("get acceptance: ", get_acceptance_yes)
        get_confirmation_yes = get_q1.filter(confirmation='Y')
        get_confirmation_no = get_q1.filter(confirmation='N')
        # if user already has chosen the confirmation, redirect to that page
        if get_acceptance_yes.count() > 0:
            if get_confirmation_yes.count() > 0:
                return render(request, 'accounts/confirm_acceptance.html')
            elif get_confirmation_no.count() > 0:
                return render(request, 'accounts/reject_acceptance.html')
            return render(request, self.template_name, {'form': form, 'apps': None})
        else:
            return redirect(reverse('home:home'))

    def post(self, request):
        user = get_object_or_404(UserProfile, user=request.user)
        form = ConfirmAcceptanceForm(request.POST, instance=user)
        if form.is_valid():
            post_data = form.save(commit=False)
            post_data.user = request.user
            post_data.save()
            form.save()
            post_q1 = UserProfile.objects.filter(user=request.user)
            post_yes = post_q1.filter(confirmation='Y')
            post_no = post_q1.filter(confirmation='N')
            if post_no.count() > 0:
                return render(request, 'accounts/reject_acceptance.html')
            else:
                user = form.save()
                sender = settings.DEFAULT_FROM_EMAIL
                recipient = [get_object_or_404(User, username=request.user).email]
                subject = 'Welcome to MedHacks: Snow Day!'
                content = render_to_string('accounts/welcome_email.html', {'user':user})
                send_mail(subject,content,sender,recipient,fail_silently=False)
                return render(request, 'accounts/confirm_acceptance.html')
        return render(request, self.template_name, {'form', form})
