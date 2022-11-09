from django.shortcuts import render
from django.http import HttpResponse
import requests
from voice.models import voice

# Create your views here.

def search(request):
    voices = voice.objects.all().order_by('-views')
    q = request.GET.get('q', "")

    if q:
        voice_list = voices.filter(title__icontains=q)
        return render(request, 'search/contents.html', {'voice': voice_list, 'q': q})

    else:
        return render(request, 'search/contents.html')


