from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, View
from .models import voice
from accounts.models import Voicemark, History

# Create your views here.
class VoiceListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = "voice/voice_map.html"
    # filtering the model
    queryset = voice.objects.order_by("-views")

class VoiceDeatilView(DetailView):
    model = voice

def toggle_voice(request, voice_pk):
    action = request.GET.get("action", None)
    voices = voice.objects.get_or_none(pk=voice_pk)
    if voices is not None and action is not None:
        the_list, _ =Voicemark.objects.get_or_create(
            user = request.user
        )
        if action == "add":
            the_list.bookmark.add(voices)
        elif action == "remove":
            the_list.bookmark.remove(voices)
    return redirect('accounts:store')

class GangwonListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = "voice/gangwondo.html"
    # filtering the model
    queryset = voice.objects.filter(region="강원도").order_by("-views")

class CbListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = "voice/chchbokdo.html"
    # filtering the model
    queryset = voice.objects.filter(region="충청북도").order_by("-views")

class CnListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = "voice/chchnamdo.html"
    # filtering the model
    queryset = voice.objects.filter(region="충청남도").order_by("-views")

class DjListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = "voice/daejeon.html"
    # filtering the model
    queryset = voice.objects.filter(region="대전광역시").order_by("-views")

class SjListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/sejong.html'
    # filtering the model
    queryset = voice.objects.filter(region="세종특별자치시").order_by("-views")

class BsListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/busan.html'
    # filtering the model
    queryset = voice.objects.filter(region="부산광역시").order_by("-views")

class DgListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/daegu.html'
    # filtering the model
    queryset = voice.objects.filter(region="대구광역시").order_by("-views")

class UsListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/ulsan.html'
    # filtering the model
    queryset = voice.objects.filter(region="울산광역시").order_by("-views")

class GnListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/gsnamdo.html'
    # filtering the model
    queryset = voice.objects.filter(region="경상남도").order_by("-views")

class GbListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/gsbokdo.html'
    # filtering the model
    queryset = voice.objects.filter(region="경상북도").order_by("-views")

class JbListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/jrabokdo.html'
    # filtering the model
    queryset = voice.objects.filter(region="전라북도").order_by("-views")

class JnListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/jranamdo.html'
    # filtering the model
    queryset = voice.objects.filter(region="전라남도").order_by("-views")

class GjListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/gwangju.html'
    # filtering the model
    queryset = voice.objects.filter(region="광주광역시").order_by("-views")

class JjnListView(ListView):
    model = voice
    # default name = "object_list"
    context_object_name = "voice_list"
    template_name = 'voice/jejudo.html'
    # filtering the model
    queryset = voice.objects.filter(region="제주특별자치도").order_by("-views")
