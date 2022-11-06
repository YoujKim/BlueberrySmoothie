from django.urls import path, include
from .views import VoiceListView,VoiceDeatilView,toggle_voice
from . import views

app_name = 'voice'

urlpatterns = [
    path('voice_map/', VoiceListView.as_view(), name='voice_map'),
    path('voice_detail/<int:pk>', VoiceDeatilView.as_view(), name='voice_detail'),
    path("toggle/<int:voice_pk>", toggle_voice, name="toggle-voice"),
    path('busan/', views.index, name="busan")
]
