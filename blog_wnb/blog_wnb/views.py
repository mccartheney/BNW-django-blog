from django.shortcuts import render

def home (request) :
    is_logged = request.user.is_authenticated
    username = request.user.username
    return render (request, "index.html", {"is_logged" : is_logged, "username" : username})