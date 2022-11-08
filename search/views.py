from django.shortcuts import render
from django.http import HttpResponse
import requests
from voice.models import voice

# Create your views here.

def search(request):
    voices = voice.objects.all().order_by('-views')

    q = request.POST.get('q', "")

    if q:
        voices = voices.filter(title__icontains=q)
        return render(request, 'contents.html', {'voice': voice, 'q': q})

    else:
        return render(request, 'search.html')


