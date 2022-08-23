from django.contrib import admin
from .models import voice

# Register your models here.
@admin.register(voice)
class voiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'region', 'views']

