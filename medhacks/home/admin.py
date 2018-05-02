from django.contrib import admin
from home.models import Application
from django.db.models.signals import post_save

# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number',
    'city', 'country', 'state', 'gender',
    'university', 'graduating_class', 'major', 'secondmajor', 'reimbursement',
    'user', 'attended', 'essay1', 'essay2', 'essay3', 'resume')

    def school_info(self, obj):
        return obj.university


admin.site.register(Application, ApplicationAdmin)
