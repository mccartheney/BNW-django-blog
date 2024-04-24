from django.urls import path

# import vies to load them on urls
from . import views

# create a app name for redirection
app_name = "users"

urlpatterns = [
    path ("", views.user_home), # path that redirect to register (if the user is logged, will be redirected to home page)
    path ("register/", views.register_view, name="register"), # path to register a user (if the user is logged, will be redirected to home page)
    path ("login/", views.login_view, name="login"), # path to login a user (if the user is logged, will be redirected to home page)
    path("logout/", views.logout_view, name="logout"), # path to logout a user (always redirect to home page)
    path("<slug:slug>/", views.profile_view, name="profile")
]