from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import RTApp
from .forms import SelectTeamForm, CreateTeamRegisterForm
from accounts.models import UserProfile
#
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

class JoinTeamView(TemplateView):
    template_name = 'registerTeamApp/joinTeam.html'

    def get(self, request):
        form = SelectTeamForm
        return render(request, self.template_name, {'form': form, 'apps': None})

    def post(self, request):
        user = get_object_or_404(UserProfile, user=request.user)
        form = SelectTeamForm(request.POST, request.FILES, instance=user)
        form2 = SelectTeamForm(request.POST, request.FILES)

        if form.is_valid():

            post_data = form.save(commit=False)
            post_data.user = request.user
            post_data.save()
            team_name = form.cleaned_data['team_name']
            form.save()
            form2.save()
            return render(request, 'registerTeamApp/registeredTeamSuccess.html')
        return render(request, self.template_name, {'form': form})
