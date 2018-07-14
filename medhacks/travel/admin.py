from django.contrib import admin
from travel.models import TRApplication
from django.db.models.signals import post_save

# Register your models here.
# We see these in admin view under application
class TRApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state', 'country', 'tr_essay',
    'contingency', 'type_reim', 'submit_time', 'travel_date_to', 'receipt_amount', 'receipt_file',
    )

    # Adds search bar
    search_fields = ['user__username']

admin.site.register(TRApplication, TRApplicationAdmin)
