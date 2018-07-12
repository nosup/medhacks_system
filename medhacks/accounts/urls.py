from django.urls import path, re_path
from home.views import HomeView
from . import views
from django.views.generic.base import RedirectView
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete,
    )
from accounts.views import ConfirmView



app_name = 'accounts'

urlpatterns = [
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    path('', HomeView.as_view(), name='home'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('login/', logout, {'template_name': 'accounts/login.html'}, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('change-password/', views.change_password, name='change_password'),

    path('reset-password/', password_reset, {'template_name':
        'accounts/reset_password.html', 'post_reset_redirect':
        'accounts:password_reset_done', 'email_template_name':
        'accounts/reset_password_email.html'}, name='reset_password'),

    # change password template for password_reset_done
    path('reset-password/done/', password_reset_done, {'template_name':
        'accounts/reset_password_done.html'}, name='password_reset_done'),


    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, {'template_name':
        'accounts/reset_password_confirm.html', 'post_reset_redirect':
        'accounts:password_reset_complete'}, name='password_reset_confirm'),


    path('reset-password/complete/', password_reset_complete, {'template_name':
        'accounts/reset_password_complete.html'},
        name='password_reset_complete')
]
