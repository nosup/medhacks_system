from django.contrib import admin
from registerTeamApp.models import RTApp, PollApp
from django.db.models.signals import post_save

# Register your models here.
# We see these in admin view under application
class RegisterTeamAppAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'votes'
    )
    # Adds search bar
    search_fields = ['user__username']

admin.site.register(RTApp, RegisterTeamAppAdmin)

class PollAppAdmin(admin.ModelAdmin):
    list_display = ('user','choice_field',
    )

admin.site.register(PollApp, PollAppAdmin)
