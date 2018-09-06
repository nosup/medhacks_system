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


def reject_travel(modeladmin, request, queryset):
    queryset.update(travel_reimbursement='Rejected')
reject_travel.short_description = "Reject TRAVEL"


def regional_travel(modeladmin, request, queryset):
    queryset.update(travel_reimbursement='Regional')
regional_travel.short_description = "Accept TRAVEL: Regional"


def midwest_travel(modeladmin, request, queryset):
    queryset.update(travel_reimbursement='Midwest')
midwest_travel.short_description = "Accept TRAVEL: Midwest"


def west_travel(modeladmin, request, queryset):
    queryset.update(travel_reimbursement='West')
west_travel.short_description = "Accept TRAVEL: West"

def international_travel(modeladmin, request, queryset):
    queryset.update(travel_reimbursement='International')
international_travel.short_description = "Accept TRAVEL: International"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'travel_reimbursement', 'travel_confirm', 'campus_ambassador', 'accepted', 'confirmation', 'registered', 'team_name')
    actions = [accept_hacker, reject_hacker, reject_travel, regional_travel, midwest_travel, west_travel, international_travel,]

    def user_info(self, obj):
        return obj.description

    # Adds search bar
    search_fields = ['user__username']

    # how to sort the queryset
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset

    # changes title/header of table
    user_info.short_description = 'Info'


admin.site.register(UserProfile, UserProfileAdmin)
