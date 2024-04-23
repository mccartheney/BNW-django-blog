from django import forms
from .models import user_profile
from django.forms import ModelForm

class register (ModelForm) :
    class Meta :
        model = user_profile
        fields = ['email', 'username', 'password', 'bio', 'profile_pic']