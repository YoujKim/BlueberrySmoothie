from django.db import models
from .choice import region_choice, situation_choice, talker_age_choice, talker_gender_choice
from . import managers
# Create your models here.

class voice(models.Model):
    title = models.CharField(max_length=50)
    region = models.CharField(max_length = 30, choices=region_choice)
    situation = models.CharField(max_length = 30, choices=situation_choice, blank=True)
    talker_age = models.CharField(max_length = 30, choices=talker_age_choice, blank=True)
    talker_gender = models.CharField(max_length = 30, choices=talker_gender_choice, blank=True)
    views = models.PositiveIntegerField(default=0)
    memo = models.CharField(max_length = 300, blank=True)
    objects = managers.CustomModelManager()

    def __str__(self):
        return self.title

    @property
    def update_views(self):
        self.views = self.views + 1
        self.save()
        return ""

class script(models.Model):
    voice = models.OneToOneField(voice, on_delete=models.CASCADE)
    memo = models.CharField(max_length= 300, blank=True)

    def __str__(self):
        return voice.title+" 대본"
