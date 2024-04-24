from django import forms

# import ModelForm to form
from django.forms import ModelForm

#import posts to create post Form for it
from .models import posts

# a form to post
class post_form (ModelForm) :
    class Meta :
        # base of the form
        model = posts

        # fields of form
        fields = ["title", "image", "description"]