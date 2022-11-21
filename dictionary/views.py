from django.shortcuts import render
from django.http import HttpResponse
from .models import Word
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'dictionary/dictionary.html')

def word_search(request):
    words = Word.objects.all().order_by('-word')
    q = request.GET.get('q', "")

    if q:
        word_list = words.filter(Q(word__icontains=q) or Q(seoul__icontaions=q))
        return render(request, 'dictionary/contents.html', {'word': word_list, 'q': q})

    else:
        return render(request, 'dictionary/contents.html')