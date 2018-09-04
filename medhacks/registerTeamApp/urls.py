from django.conf.urls import url
from django.urls import path, include
from registerTeamApp.views import RegisterTeamView, JoinTeamView


app_name = 'registerTeamApp'
urlpatterns = [
    path('join/', JoinTeamView.as_view(), name='joinTeam'),
    path('', RegisterTeamView.as_view(), name='registerTeamApp')
]
