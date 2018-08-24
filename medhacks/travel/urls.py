from django.conf.urls import url
from django.urls import path, include
from travel.views import TravelView, RecieptView, TravelHomeView


app_name = 'travel'
urlpatterns = [
    path('status/', TravelHomeView.as_view(), name='travel_home'),
    path('', TravelView.as_view(), name='travel'),
    path('receipt_submission/', RecieptView.as_view(), name='receipt')
]
