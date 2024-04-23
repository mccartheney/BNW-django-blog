from django.db import models
from django.contrib.auth.models import User

class user_profile (models.Model) :
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to="profile_pics/", default="user.png")
    slug = models.SlugField(default="")

    def __str__(self) :
        return self.username