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

def index(request):
    return render(request, 'voice/busan.html')