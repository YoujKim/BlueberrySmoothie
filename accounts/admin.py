from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Profile,Voicemark,History

# Define an inline admin descriptor for profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class VoicemarkInline(admin.StackedInline):
    model = Voicemark
    can_delete = False
    verbose_name_plural = 'voicemark'

class HistoryInline(admin.StackedInline):
    model = History
    can_delete = False
    verbose_name_plural = 'history'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, VoicemarkInline, HistoryInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

