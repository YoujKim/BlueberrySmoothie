from django.urls import path, include
from . import views

app_name = 'gyeongsang'

urlpatterns = [
    path('', views.index, name='gyeongsang')
]