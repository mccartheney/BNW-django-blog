from django.db import models

# create model for posts
class posts (models.Model) :
    made_by = models.CharField (default="", max_length=50)
    image = models.ImageField (upload_to="posts_pics/")
    title = models.CharField (max_length=100)
    description = models.TextField (default="")
    content_id = models.TextField(default="")
    slug = models.SlugField(default="")

    # define "name" for model
    def __str__ (self) :
        return f"{self.title} <{self.made_by}> "

