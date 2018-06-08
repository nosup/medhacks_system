from django.contrib import admin
from travel.models import TRApplication
from django.db.models.signals import post_save

# Register your models here.
# We see these in admin view under application
class TRApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state', 'country', 'tr_essay',
    'contingency', 'type_reim', 'submit_time',
    )

admin.site.register(TRApplication, TRApplicationAdmin)
