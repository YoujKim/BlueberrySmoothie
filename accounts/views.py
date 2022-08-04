from django.shortcuts import render
from django.views.generic import TemplateView

#추후 view 수정 필요
class InfoList(TemplateView):
    template_name = 'accounts/mypage.html'

class StudyList(TemplateView):
    template_name = 'accounts/study.html'

class StoreList(TemplateView):
    template_name = 'accounts/voice_store.html'

class WstoreList(TemplateView):
    template_name = 'accounts/word_store.html'
