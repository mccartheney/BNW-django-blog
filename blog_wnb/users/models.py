from django.db import models

# creating model user_profile
class user_profile (models.Model) :
    # setting camps for that model
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    bio = models.TextField(default="")
    profile_pic = models.ImageField(upload_to="profile_pics/", default="user.png")
    slug = models.SlugField(default="")

    # set the "name" of the model
    def __str__(self) :
        return f"{self.username} <{self.email}>"