from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import RTApp
from .forms import CreateTeamRegisterForm
from accounts.models import UserProfile
from home.models import Application

class RegisterTeamView(TemplateView):
    template_name = 'registerTeamApp/registerTeamApp.html'

    def get(self, request):
        form = CreateTeamRegisterForm
        return render(request, self.template_name, {'form': form, 'apps': None})

    def post(self, request):
        form = CreateTeamRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            team_name = form.cleaned_data['team_name']

            form.save()
            #return render(request, 'registerTeamApp/registeredTeamSucess.html')
            return render(request, 'home/applied.html')
        return render(request, self.template_name, {'form': form})
