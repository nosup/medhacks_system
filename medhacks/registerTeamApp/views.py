from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import RTApp, PollApp
from .forms import SelectTeamForm, CreateTeamRegisterForm, VotePollForm
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

        if form.is_valid():

            post_data = form.save(commit=False)
            post_data.user = request.user
            post_data.save()

            team_name = form.cleaned_data['team_name']

            team = RTApp.objects.get(team_name=team_name)
            form2 = SelectTeamForm(request.POST, request.FILES, instance=team)
            team.users.add(request.user) # Add the M2M relationship

            form.save()
            form2.save()
            return render(request, 'registerTeamApp/registeredTeamSuccess.html')
        return render(request, self.template_name, {'form': form})


class PollTeamView(TemplateView):
    template_name = 'registerTeamApp/votePollTeam.html'

    def get(self, request):
        form = VotePollForm

        votes = PollApp.objects.filter(user=request.user)[:1]

        if votes.count() > 0:
            return render(request, self.template_name, {'form': None})

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = VotePollForm(request.POST, request.FILES)
        if form.is_valid():
            choice_field = form.cleaned_data['choice_field']

            form.save()
            #return render(request, 'registerTeamApp/registeredTeamSucess.html')
            return render(request, 'home/applied.html')
        return render(request, self.template_name, {'form': form})
