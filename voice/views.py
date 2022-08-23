from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import voice

# Create your views here.
class VoiceListView(ListView):
    model = voice
    # default name = "objcet_list"
    context_object_name = "voice_list"
    # filtering the model
    queryset = voice.objects.order_by("-views")

class VoiceDeatilView(DetailView):
    model = voice