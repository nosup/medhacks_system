from django.contrib import admin
from accounts.models import UserProfile
from django.db.models.signals import post_save

# Register your models here.
def accept_hacker(modeladmin, request, queryset):
    queryset.update(accepted='Y')
accept_hacker.short_description = "Accept selected users into MedHacks"

def reject_hacker(modeladmin, request, queryset):
    queryset.update(accepted='N')
reject_hacker.short_description = "Reject selected users"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'travel_reimbursement', 'campus_ambassador', 'accepted')
    actions = [accept_hacker, reject_hacker,]

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
