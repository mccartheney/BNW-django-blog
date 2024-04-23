from django.shortcuts import render, redirect

# import login required to make a login required pages
from django.contrib.auth.decorators import login_required

# import post_form to get info from user to create a new form 
from .forms import post_form

# import slugfy to slugfy
from django.utils.text import slugify

# import uuid to create a new unique id
import uuid

# import user_profile from user models to get info about logged user
from users.models import user_profile


@login_required(login_url="users:login") # if user is not logged send him to users:login
def create_post (request) :
    # Get username (email) from user
    user_email = request.user.username

    # getting user from user_profile models by email
    user = user_profile.objects.filter( email = user_email )[0]

    # verify if  request method is post
    if request.method == "POST" : # if it is
        # get form data and files
        form = post_form(request.POST, request.FILES)

        # if its ok with form
        if form.is_valid () :
            # create a unique id with uuid
            new_id = uuid.uuid4()

            # get form data
            form_data= form.cleaned_data

            # create a slug for the form 
            slug = slugify (f"{form_data['title']} <{new_id}> <{user_email}>")

            # set values that dont come with the form but its necessary for the model
            form.instance.slug = slug
            form.instance.made_by = user_email
            form.instance.content_id = new_id

            # save form data
            form.save()

            # redirect to home
            return redirect ("/")
 
    else : # if method is not post
        form = post_form()

    # return create post page
    return render (request, "posts/create_post.html", {
        "form" : form, 
        "user" : user, 
        "is_logged" : True,
        })