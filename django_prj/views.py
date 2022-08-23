from django.views.generic import TemplateView, ListView
from voice.models import voice

#TemplateView
class HomeView(ListView):
    template_name = 'home.html'
    model = voice
    context_object_name = "voice_list"
    queryset = voice.objects.order_by("-views")[0:5]