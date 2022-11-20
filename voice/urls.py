from django.urls import path, include
from .views import VoiceListView,VoiceDeatilView,toggle_voice,GangwonListView,CbListView,CnListView,DjListView,SjListView,\
    BsListView,DgListView,UsListView,GnListView,GbListView,JbListView,JnListView,GjListView,JjnListView
from . import views

app_name = 'voice'

urlpatterns = [
    path('voice_map/', VoiceListView.as_view(), name='voice_map'),
    path('voice_detail/<int:pk>', VoiceDeatilView.as_view(), name='voice_detail'),
    path("toggle/<int:voice_pk>", toggle_voice, name="toggle-voice"),
    path('voice_map/gangwondo/', GangwonListView.as_view(), name="gangwondo"),
    path('voice_map/chchbokdo/', CbListView.as_view(), name="chchbokdo"),
    path('voice_map/chchnamdo/', CnListView.as_view(), name="chchnamdo"),
    path('voice_map/daejeon/', DjListView.as_view(), name="daejeon"),
    path('voice_map/sejong/', SjListView.as_view(), name="sejong"),
    path('voice_map/busan/', BsListView.as_view(), name="busan"),
    path('voice_map/gsnamdo/', GnListView.as_view(), name="gsnamdo"),
    path('voice_map/gsbokdo/', GbListView.as_view(), name="gsbokdo"),
    path('voice_map/ulsan/', UsListView.as_view(), name="ulsan"),
    path('voice_map/daegu/', DgListView.as_view(), name="daegu"),
    path('voice_map/jrabokdo/', JbListView.as_view(), name="jrabokdo"),
    path('voice_map/jranamdo/', JnListView.as_view(), name="jranamdo"),
    path('voice_map/gwangju/', GjListView.as_view(), name="gwangju"),
    path('voice_map/jejudo/', JjnListView.as_view(), name="jejudo")
]
