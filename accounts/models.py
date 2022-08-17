from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 자기소개
    description = models.CharField(max_length=300, blank=True)
    # 지역
    location = models.CharField(max_length=20, blank=True)

