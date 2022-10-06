from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def contents(request):

    try:
        ticker = request.GET['ticker']
        #""안에 voice파일 중 제일 첫번째꺼
        search = requests.get("http://127.0.0.1:8000/voice/voice_detail/1")
    except Exception as e:
        search = ""

    content = {'search':search}

    return render(request, 'search/contents.html', content)


