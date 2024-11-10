from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("honey_app.urls")),
    path('',include("user.urls")),
    path('',include("user_honey.urls")),
]