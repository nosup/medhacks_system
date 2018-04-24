from django.contrib import admin
from home.models import Application
from django.db.models.signals import post_save

# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number',
    'address1', 'address2', 'zipcode', 'city', 'country', 'gender',
    'university', 'graduating_class', 'major', 'reimbursement',
    'user', 'essay1', 'essay2', 'essay3', 'resume')

    def school_info(self, obj):
        return obj.university


admin.site.register(Application, ApplicationAdmin)
