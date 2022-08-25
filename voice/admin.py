from django.contrib import admin
from .models import voice,script

# Register your models here.
@admin.register(voice)
class voiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'region', 'views']

admin.register(script)
