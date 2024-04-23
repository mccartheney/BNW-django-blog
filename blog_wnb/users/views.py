from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .forms import register
from .models import user_profile

def user_home(request):
    return redirect('users:login')

def register_view(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user_data = form.save()
    #         auth_login(request, user_data)
    #         return redirect('/')
    # else:
    #     form = UserCreationForm()
    
    if request.method == "POST" :
        form = register(request.POST, request.FILES)
        if form.is_valid () :
            email_from_form = form.cleaned_data["email"]
            user_profile_exists = user_profile.objects.filter(email=email_from_form).exists()
            if user_profile_exists :
                warn_message = " ⚠️ This email is alredy been used, try another "
                return render(request, "users/register.html", {'form': form, "message": warn_message})

            else :
                form_data = form.cleaned_data

                User.objects.update_or_create (
                    email = form_data ["email"],
                    username = form_data ["username"],
                    password = form_data ["password"]
                )

                form.save()
                return redirect("/")

    else :
        form = register()
    return render(request, "users/register.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')  
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")