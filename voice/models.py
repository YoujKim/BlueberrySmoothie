from django.db import models
from .choice import region_choice, situation_choice, talker_age_choice, talker_gender_choice
from . import managers
import os
from django.contrib.auth.models import User
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
    audio = models.FileField(upload_to="voice")
    script = models.FileField(upload_to="script", blank=True)
    script_title = models.CharField(max_length=100, blank=True)
    text = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title

    @property
    def update_views(self):
        self.views = self.views + 1
        self.save()
        return ""

    @property
    def upload_text(self):
        if self.text == "":
            file_path = 'media/script/'+self.script_title+'.txt'
            script = ""

            try:
                f=open(file_path,'r',encoding="UTF-8")
                while True:
                    line = f.readline()
                    if not line: break
                    script = script + line
                self.text = script
                self.save()
                f.close()
            except:
                print("파일이 존재하지 않습니다")
        return ""
