# import render to render return rendered html to user
from django.shortcuts import render

# import user_profile from user models to get info about logged user
from users.models import user_profile

# import posts to get posts to show in home page
from posts.models import posts

from django.contrib.auth import logout

# function to logout superuser
def loggout_superuser (is_super_user) :
    # if user is super user 
    if is_super_user:
        # logout and send to home page
        logout(request)
        return redirect("/")

# define home view
def home (request) :
    # logout super user
    loggout_superuser(request.user.is_superuser)

    # get first ten posts
    all_posts = posts.objects.all()[0:10]
    # create array to get posts and users
    posts_and_users = []

    # loop through posts
    for post in all_posts :
        # get post creator
        creator = user_profile.objects.filter(email=post.made_by)[0]

        # append post and creator to array
        posts_and_users.append({
            "post" : post,
            "creator" : creator
        })


    # if user is logged = True, if not = False
    is_logged = request.user.is_authenticated

    # verify if user is logged
    if (is_logged) : # if is logged
        # Get username (email) from user
        user_email = request.user.username

        # getting user from user_profile models by email
        user = user_profile.objects.filter( email = user_email )[0]

        # return index.html with some "arguments" : is logged, posts and user
        return render (request, "index.html", {
            "is_logged" : is_logged, 
            "user" : user,
            "posts_and_users" : posts_and_users[::-1]
        })
        
    else : # if its not logged
        user_name = ""

    # return index.html with some "arguments" : is logged, posts
    return render (request, "index.html", {
        "is_logged" : is_logged,
        "posts_and_users" : posts_and_users[::-1],
    })