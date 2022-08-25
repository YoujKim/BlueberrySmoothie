from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .forms import UserUpdateForm
from .models import Profile,Voicemark
from voice.models import voice


class InfoList(TemplateView):
    template_name = 'accounts/mypage.html'

class StudyList(TemplateView):
    template_name = 'accounts/study.html'

class StoreList(TemplateView):
    template_name = 'accounts/store.html'

def update(request):
    try:
        if request.method == "POST":
            form = UserUpdateForm(request.POST, instance=request.user.profile) 
            if form.is_valid():
                form.save()
                return redirect('accounts:mypage')
        else:
            form = UserUpdateForm(instance=request.user.profile)
        return render(request, 'accounts/update.html', {'form': form})
    except:
            profile = Profile(location="", description="", user=request.user)
            profile.save()
            return redirect('accounts:update')
