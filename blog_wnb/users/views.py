from django.shortcuts import render, redirect

def user_home (request) :
    return redirect (request, "users:login")

def register_view (request) :
    return render (request, "users/register.html")

def login_view (request) :
    return render (request, "users/login.html")
