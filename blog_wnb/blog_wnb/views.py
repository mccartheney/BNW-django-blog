# import render to render return rendered html to user
from django.shortcuts import render

# import user_profile from user models to get info about logged user
from users.models import user_profile

# define home view
def home (request) :
    # if user is logged = True, if not = False
    is_logged = request.user.is_authenticated

    # verify if user is logged
    if (is_logged) : # if is logged
        # Get username (email) from user
        user_email = request.user.username

        # getting user from user_profile models by email
        user = user_profile.objects.filter( email = user_email )[0]
    
        # return index.html with some "arguments" : is logged and user
        return render (request, "index.html", {
            "is_logged" : is_logged, 
            "user" : user
        })
        
    else : # if its not logged
        user_name = ""

    # return index.html with some "arguments" : is logged
    return render (request, "index.html", {
        "is_logged" : is_logged,
    })