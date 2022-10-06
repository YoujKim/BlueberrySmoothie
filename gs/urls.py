from django.urls import path, include
from . import views

app_name = 'gs'

urlpatterns = [
    path('', views.index, name='gs')
]