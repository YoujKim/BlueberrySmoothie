from django.db import models
from .choice import region_choice

# Create your models here.

class Word(models.Model):
    # 단어(사투리)
    word = models.CharField(max_length=50)
    # 지역
    region = models.CharField(max_length = 30, choices=region_choice)
    # 표준어
    seoul = models.CharField(max_length=50)
    # 예문(사투리)
    ex_word = models.CharField(max_length=500, default="")
    # 예문(표준어)
    ex_seoul = models.CharField(max_length= 500, default="")

    def __str__(self):
        return self.word
    

