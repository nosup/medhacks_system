from django.conf.urls import url
from django.urls import path, include
from home.views import HomeView


app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home')
] 
