from django import forms
from .models import Profile
from django.contrib.auth import get_user_model

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'description']
        widgets = {
            'location': forms.Select(),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "자기 소개"
            }),
        }