from django.urls import path, include
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.index, name='dictionary'),
    path('contents', views.word_search, name="search"),
]