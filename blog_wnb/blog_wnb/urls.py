from django.contrib import admin
from django.urls import path, include
 
# import things to turn possible get media
from django.conf.urls.static import static
from django.conf import settings

# urls for app
urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls"))
]

# url for app get media
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)