from django.contrib import admin
from django.urls import path, include
from django_prj.views import HomeView
from . import views

app_name = 'search'

urlpatterns = [
    path('',views.search, name='search'),
]

