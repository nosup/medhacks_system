from django.contrib import admin
from home.models import Application
from django.db.models.signals import post_save

# Register your models here.
# We see these in admin view under application
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone_number',
    'city', 'state', 'country', 'gender','education',
    'university', 'graduating_class', 'major', 'secondmajor', 'reimbursement',
    'attended', 'essay1', 'essay2', 'essay3', 'essay4', 'resume', 'submit_time',)

    def school_info(self, obj):
        return obj.university


admin.site.register(Application, ApplicationAdmin)
