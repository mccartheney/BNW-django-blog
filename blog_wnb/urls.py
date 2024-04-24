from django.contrib import admin
from django.urls import path, include
 
from . import views

# import things to turn possible get media
from django.conf.urls.static import static
from django.conf import settings

# urls for app
urlpatterns = [
    path('admin/', admin.site.urls), # for admin
    path("", views.home), # route for home 
    path("users/", include("users.urls")), # route for users app
    path("posts/", include("posts.urls")) # route for users app
]

# url for app get media
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)