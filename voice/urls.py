from django.urls import path, include
from .views import VoiceListView,VoiceDeatilView,toggle_voice

app_name = 'voice'

urlpatterns = [
    path('voice_list/', VoiceListView.as_view(), name='voice_list'),
    path('voice_detail/<int:pk>', VoiceDeatilView.as_view(), name='voice_detail'),
    path("toggle/<int:voice_pk>", toggle_voice, name="toggle-voice"),
]
