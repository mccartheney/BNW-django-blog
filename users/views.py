# import render to render a page and redirect to redirect to some page
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


# import login as auth_login to login a user and as auth_login because login() was given error, 
# logout to logout, 
# authenticate to return a user when gives a username and password 
from django.contrib.auth import login as auth_login, logout, authenticate

# import users to login, register or logout
from django.contrib.auth.models import User

# import custom forms
from .forms import register_form, login_form

# import user_profile model
from .models import user_profile

# import posts model
from posts.models import posts

# import slugfy to slugfy username 
from django.utils.text import slugify

# import uuid to create a unique id
import uuid

# function to logout superuser
def loggout_superuser (is_super_user) :
    # if user is super user 
    if is_super_user:
        # logout and send to home page
        logout(request)
        return redirect("/")

# a view with a funtion to redirect to login view
def user_home(request):
    # logout super user
    loggout_superuser(request.user.is_superuser)

    # redirect to login page 
    return redirect('users:login')

# a view with funtion to register a person
def register_view(request):
    # logout super user
    loggout_superuser(request.user.is_superuser)

    # get info from user if its logged or not
    is_logged = request.user.is_authenticated

    # if the user is not logged
    if not is_logged :

        # verify if the method of request is POST
        if request.method == "POST" : # if it is
            # get the form values
            form = register_form(request.POST, request.FILES)

            if form.is_valid () : # if its ok with the form values
                # get email from form
                email_from_form = form.cleaned_data["email"]

                # get user_profile existence from email 
                user_profile_exists = user_profile.objects.filter(email=email_from_form).exists()

                if user_profile_exists : # if user profile exists
                    # return login page, warning that user alredy exists
                    warn_message = " ⚠️ This email is alredy been used, try another "
                    return render(request, "users/register.html", {'form': form, "message": warn_message})

                else : # if user profile dont exists
                    # get data from form
                    form_data = form.cleaned_data

                    # create a user with data from form
                    User.objects.create_user (
                        email = form_data ["email"],
                        username = form_data ["email"],
                        password=form_data["password"],
                    )

                    # create a unique id with uuid
                    new_id = uuid.uuid4()

                    #  set id user as new_id
                    form.instance.user_id = new_id

                    # Generate slug based on username
                    slug = slugify(new_id)

                    # # # Add the slug to the form data
                    form.instance.slug = slug

                    # save user user profile to database
                    form.save()

                    # redirect to home
                    return redirect("/")

        else : # if the method is 
            form = register_form()
        
        # return login page
        return render(request, "users/register.html", {'form': form})
    else : # if user is logged
        # redirect to home page
        return redirect("/")

# a view with funtion to login a user 
def login_view(request):
    loggout_superuser(request.user.is_superuser)


    # get info if user is logged
    is_logged = request.user.is_authenticated

    if not is_logged : # if user is not logged

        # verify if request.method is POST
        if request.method == 'POST': # if it is
            # get form info
            form = login_form(request.POST)
            if form.is_valid(): # if its ok with form data
                # get data from from
                form_data = form.cleaned_data

                # get user_profile by email from form
                user_get_profile = user_profile.objects.filter(email = form_data["email"])
                #verify id user_profile exist
                user_exists = user_get_profile.exists()

                if user_exists : # if user profile exists
                    # get the user_profile
                    user_profile_data = user_get_profile[0]

                    # get username from user_profile and password from form
                    username_data = user_profile_data.email
                    password_data = form_data["password"]
                    
                    # verify if the user exists
                    user = authenticate(request, username=username_data, password=password_data)
                    
                    if user is not None: # if have a user
                        # login the user
                        auth_login(request, user)

                        # redirect to home
                        return redirect('/')

                    else : # if user enter wrong credential
                        # return login page warning the user send wrong credencials
                        warn_message = "⚠️ Wrong credencials" 
                        return render(request, "users/login.html", {'form': form, "message" : warn_message})

                
                else : # if user dont exist
                    # return login page and warn to user that accont dont exists 
                    warn_message = " ⚠️ Dont exist a account with that email, login with a existent email or register "
                    return render(request, "users/login.html", {'form': form, "message" : warn_message})

        else: # if method is not POST
            # create form to login
            form = login_form()

        # return login page
        return render(request, "users/login.html", {'form': form})
    else : # if user is logged
        # redirect to home
        return redirect("/")

# a view with funtion of loggout a user
def logout_view(request):
    # loggout user
    logout(request)

    # redirect to home
    return redirect("/")

@login_required(login_url="users:login") # if user is not logged send him to users:login
# view to check profile info and delete account or a post
def my_profile_view (request) : 
    # logout super user
    loggout_superuser(request.user.is_superuser)

    if request.method == "POST" : # if mehod is post
        if "delete_post" in request.POST : # check if info send from user is delete post
            # get   data sent by user
            search_id = request.POST["delete_post"]

            # search post by data
            post_to_delete = posts.objects.filter(content_id=search_id)[0]

            # delte post
            post_to_delete.delete()

        elif "delete_account" in request.POST : # check if info sent from user is deleted post
            # get user profile with user data
            user_profile_account_to_delete = user_profile.objects.filter(email=request.user.username)[0]
            # get user with user data
            user_account_to_delete = User.objects.filter(username=user_profile_account_to_delete.email)[0]

            # loggout user to delete account
            logout(request)

            # delete account 
            user_account_to_delete.delete()
            user_profile_account_to_delete.delete()

            # redirect to home
            return redirect("/")


    # if user is logged = True, if not = False
    is_logged = request.user.is_authenticated

    search_user = user_profile.objects.filter(email=request.user.username)

    user = search_user[0]
    user_content_posts = posts.objects.filter(made_by=user.email)
    posts_and_users = []

    for post in user_content_posts :
        posts_and_users.append({
            "post" : post,
            "creator" : user
        })

    return render (request, "users/my_profile.html", {
        "is_logged" : is_logged,
        "posts_and_users" : posts_and_users[::-1],
        "user" : user
    })

def profile_view (request, slug) :
    loggout_superuser(request.user.is_superuser)

    is_logged = request.user.is_authenticated

    search_user = user_profile.objects.filter(slug=slug)

    if len(search_user) > 0 :
        user = search_user[0]
        user_content_posts = posts.objects.filter(made_by=user.email)
        posts_and_users = []

        for post in user_content_posts :
            posts_and_users.append({
                "post" : post,
                "creator" : user
            })

    
    return render (request, "users/user_profile.html", {
        "is_logged" : is_logged,
        "posts_and_users" : posts_and_users[::-1],
        "user" : user
    })