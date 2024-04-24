from django import forms

# import user_profile from models
from .models import user_profile

# import modelForm to use it as base for customs form
from django.forms import ModelForm

# create a class (form) Register_form with ModelForm as base
class register_form (ModelForm) :
    # setting data for form
    class Meta :
        # using user_profile model to create that model
        model = user_profile

        # setting which camps from user_profile will show
        fields = ['email', 'username', 'password', 'bio', 'profile_pic']

        # setting password hidden widget to password input
        widgets = {
            'password': forms.PasswordInput()
        }

# create a class (form) login_form with ModelForm as base
class login_form (ModelForm) :
    # setting data for form
    class Meta :
        # using user_profile model to create that model
        model = user_profile

        # setting which camps from user_profile will show
        fields = ["email", "password"]

        # setting password hidden widget to password input
        widgets = {
            'password': forms.PasswordInput()
        }