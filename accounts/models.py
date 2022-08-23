from django.db import models
from django.contrib.auth.models import User

region_choice = (
    ('강원도','강원도'),
    ('경상북도','경상북도'),
    ('경상남도','경상남도'),
    ('전라북도','전라북도'),
    ('전라남도','전라남도'),
    ('제주특별자치도','제주특별자치도'),
    ('충청북도','충청남도'),
    ('광주광역시','광주광역시'),
    ('대구광역시','대구광역시'),
    ('부산광역시','부산광역시'),
    ('울산광역시','울산광역시'),
    ('서울특별시','서울특별시'),
    ('인천광역시','인천광역시'),
    ('대전광역시','대전광역시'),
    ('경기도','경기도'),
    ('세종특별자치시','세종특별자치시')
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 자기소개
    description = models.CharField(max_length=300, blank=True)
    # 지역
    location = models.CharField(max_length = 30, choices=region_choice, blank=True)

