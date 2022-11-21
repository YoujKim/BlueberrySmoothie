from django.db import models
from .choice import region_choice,pos_choice

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=50)
    region = models.CharField(max_length = 30, choices=region_choice)
    # 서울말
    seoul = models.CharField(max_length=50)
    # 뜻 풀이
    mean = models.CharField(max_length=500, default="")
    # 품사
    pos = models.CharField(max_length= 30, choices = pos_choice)

    def __str__(self):
        return self.word
    

