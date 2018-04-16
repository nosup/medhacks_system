from django.contrib import admin
from accounts.models import UserProfile
from django.db.models.signals import post_save

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'travel_reimbursement', 'campus_ambassador',)

    def user_info(self, obj):
        return obj.description

    # how to sort the queryset
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset

    # changes title/header of table
    user_info.short_description = 'Info'


admin.site.register(UserProfile, UserProfileAdmin)
