from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.models import User

from .forms import register_form, login_form
from .models import user_profile

def user_home(request):
    return redirect('users:login')

def register_view(request):
    is_logged = request.user.is_authenticated
    if not is_logged :

        if request.method == "POST" :
            form = register_form(request.POST, request.FILES)
            if form.is_valid () :
                email_from_form = form.cleaned_data["email"]
                user_profile_exists = user_profile.objects.filter(email=email_from_form).exists()
                if user_profile_exists :
                    warn_message = " ⚠️ This email is alredy been used, try another "
                    return render(request, "users/register.html", {'form': form, "message": warn_message})

                else :
                    form_data = form.cleaned_data

                    new_user = User.objects.create_user (
                        email = form_data ["email"],
                        username = form_data ["username"],
                        password=form_data["password"],
                    )

                    form.save()
                    return redirect("/")

        else :
            form = register_form()
        return render(request, "users/register.html", {'form': form})
    else :
        return redirect("/")


def login_view(request):
    is_logged = request.user.is_authenticated
    if not is_logged :

        if request.method == 'POST':
            form = login_form(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                user_get_profile = user_profile.objects.filter(email = form_data["email"])
                user_exists = user_get_profile.exists()


                if user_exists :
                    user_profile_data = user_get_profile[0]

                    username_data = user_profile_data.username
                    password_data = form_data["password"]

                    user = authenticate(request, username=username_data, password=password_data)
                    if user is not None:
                        # Authentication succeeded
                        auth_login(request, user)
                        return redirect('/')

                    else :
                        warn_message = "⚠️ Wrong credencials" 
                        return render(request, "users/login.html", {'form': form, "message" : warn_message})

                else :
                    warn_message = " ⚠️ Dont exist a account with that email, login with a existent email or register "
                    return render(request, "users/login.html", {'form': form, "message" : warn_message})

        else:
            form = login_form()
        return render(request, "users/login.html", {'form': form})
    else :
        return redirect("/")
        

def logout_view(request):
    logout(request)
    return redirect("/")