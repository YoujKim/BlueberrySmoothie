from django.shortcuts import render
from django.views.generic import TemplateView

#���� view ���� �ʿ�
class InfoList(TemplateView):
    template_name = 'accounts/mypage.html'

class StudyList(TemplateView):
    template_name = 'accounts/study.html'

class StoreList(TemplateView):
    template_name = 'accounts/store.html'
