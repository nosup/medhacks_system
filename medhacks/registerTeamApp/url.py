from django.conf.urls import url
from django.urls import path, include
from registerTeamApp.views import RegisterTeamView


app_name = 'home'
urlpatterns = [
    #path('', TravelView.as_view(), name='registerTeamApp'),
    path('', RegisterTeamView.as_view(), name='registerteam')
]
