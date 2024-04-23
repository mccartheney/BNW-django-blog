# import render to render return rendered html to user
from django.shortcuts import render

# define home view
def home (request) :
    # if user is logged = True, if not = False
    is_logged = request.user.is_authenticated

    # Get username from user
    username = request.user.username

    # return inde.html with some "arguments"
    return render (request, "index.html", {
        "is_logged" : is_logged, 
        "username" : username
    })