from django.contrib import admin

# import user_profile model to give admin authorization to add/remove or edit user_profiles
from .models import user_profile

# give admin authorization to user_profile
admin.site.register(user_profile)
