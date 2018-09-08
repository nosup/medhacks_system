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


            if not RTApp.objects.filter(team_name=team_name).exists():
                users = request.user # Add the M2M relationship
                form.save()
                return render(request, 'registerTeamApp/registeredTeamSuccess.html')


            team = RTApp.objects.get(team_name=team_name)
            form2 = SelectTeamForm(request.POST, request.FILES, instance=team)

            if team.users.count() >= 5:
                return render(request, 'registerTeamApp/errorform.html')
            team.users.add(request.user) # Add the M2M relationship

            form.save()
            form2.save()
            return render(request, 'registerTeamApp/registeredTeamSuccess.html')
        return render(request, self.template_name, {'form': form})


class PollTeamView(TemplateView):
    template_name = 'registerTeamApp/votePollTeam.html'

    def get(self, request):
        form = VotePollForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user = get_object_or_404(UserProfile, user=request.user)
        form = VotePollForm(request.POST, request.FILES)
        if form.is_valid():
            choice_field = form.cleaned_data['choice_field']
            for choice in choice_field:
                if RTApp.objects.filter(team_name=choice).count() > 0:
                    team = RTApp.objects.filter(team_name=choice)[0]
                    team.votes += 1
                else:
                    team = RTApp(team_name=choice, votes = 1)
                    team.team_name = choice
                team.save()
            user.voted = 1
            user.save()
            return render(request, 'registerTeamApp/voted.html')
        return render(request, self.template_name, {'form': form})
