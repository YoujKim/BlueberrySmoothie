from django.urls import path, include
from .views import VoiceListView,VoiceDeatilView

app_name = 'voice'

urlpatterns = [
    path('voice_list/', VoiceListView.as_view(), name='voice_list'),
    path('voice_detail/<int:pk>', VoiceDeatilView.as_view(), name='voice_detail'),
]
