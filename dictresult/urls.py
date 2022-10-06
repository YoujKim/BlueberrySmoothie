from django.urls import path, include
from . import views

app_name = 'dictresult'

urlpatterns = [
    path('', views.index, name='dictresult')
]