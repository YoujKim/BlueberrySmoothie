from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def contents(request):

    try:
        ticker = request.GET['ticker']
        #""안에 jason형식으로 출력되는 api 작성 일단 네이버로 넣어놓음
        search_api = requests.get("https://openapi.naver.com/v1/search/blog/"+ ticker +".json")  
        search = json.loads(search_api.content)
    except Exception as e:
        search = ""

    content = {'search':search}

    return render(request, 'search/contents.html', content)
