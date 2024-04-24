from django.contrib import admin

# import posts to give acess to admin
from .models import posts

# give acess to post for admin
admin.site.register(posts)
