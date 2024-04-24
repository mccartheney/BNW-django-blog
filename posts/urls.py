from django.urls import path

# import views to show views to user
from . import views

# declaring a app name to redirect to this app
app_name = "posts"

urlpatterns = [
    path("createpost/", views.create_post, name="newpost") # path to create new post
]