from django.contrib import admin
from .models import voice,script

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = script
    can_delete = False
    verbose_name_plural = 'script'

@admin.register(voice)
class voiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'region', 'views']
    inlines = (ProfileInline, )

admin.register(voice, voiceAdmin)
