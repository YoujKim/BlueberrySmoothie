from django.urls import path, include
from .views import VoiceListView,VoiceDeatilView,toggle_voice
from . import views

app_name = 'voice'

urlpatterns = [
    path('voice_map/', VoiceListView.as_view(), name='voice_map'),
    path('voice_detail/<int:pk>', VoiceDeatilView.as_view(), name='voice_detail'),
    path("toggle/<int:voice_pk>", toggle_voice, name="toggle-voice"),
    path('gwdo/gangwondo/', views.index, name="gangwondo"),
    path('chchdo/chchbokdo/', views.index, name="chchbokdo"),
    path('chchdo/chchnamdo/', views.index, name="chchnamdo"),
    path('chchdo/daejeon/', views.index, name="daejeon"),
    path('chchdo/sejong/', views.index, name="sejong"),
    path('gsdo/busan/', views.index, name="busan"),
    path('gsdo/gsnamdo/', views.index, name="gsnamdo"),
    path('gsdo/gsbokdo/', views.index, name="gsbokdo"),
    path('gsdo/ulsan/', views.index, name="ulsan"),
    path('gsdo/daegu/', views.index, name="daegu"),
    path('jrado/jrabokdo/', views.index, name="jrabokdo"),
    path('jrado/jranamdo/', views.index, name="jranamdo"),
    path('jrado/gwangju/', views.index, name="gwangju"),
    path('jeju/jejudo/', views.index, name="jejudo")
]
