from django import forms
from .models import user_profile
from django.forms import ModelForm

class register_form (ModelForm) :
    class Meta :
        model = user_profile
        fields = ['email', 'username', 'password', 'bio', 'profile_pic']
        widgets = {
            'password': forms.PasswordInput()
        }
class login_form (ModelForm) :
    class Meta :
        model = user_profile
        fields = ["email", "password"]
        widgets = {
            'password': forms.PasswordInput()
        }