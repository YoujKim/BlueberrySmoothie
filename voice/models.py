from django.db import models
from .choice import region_choice, situation_choice, talker_choice, gender_choice
# Create your models here.

class Voice(models.Model):
    title = models.CharField(max_length=50)
    region = models.CharField(max_length = 30, choices=region_choice)
    situation = models.CharField(max_length = 30, choices=situation_choice, blank=True)
    talker = models.CharField(max_length = 30, choices=talker_choice, blank=True)
    gender = models.CharField(max_length = 30, choices=gender_choice, blank=True)
    views = models.IntegerField(default=0)
    memo = models.CharField(max_length = 300, blank=True)
