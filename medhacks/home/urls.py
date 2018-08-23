from django.conf.urls import url
from django.urls import path, include
from home.views import HomeView
from home.views import ProfileView


app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
