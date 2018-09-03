from django.conf.urls import url
from django.urls import path, include
from registerTeamApp.views import RegisterTeamView


app_name = 'registerTeamApp'
urlpatterns = [
    #path('register_success/', logout, {'template_name': 'accounts/login.html'}, name='logout'),
    path('', RegisterTeamView.as_view(), name='registerTeamApp')
]
