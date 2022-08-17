from django import forms
from .models import Profile
from django.contrib.auth import get_user_model

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'description']
        widgets = {
            'location': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': "거주 지역"
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "자기 소개"
            }),
        }