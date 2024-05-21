from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin.html/", admin.site.urls),
    path("auth/", include("auth.urls")),
    path("", include("homepage.urls")),
    path("app/", include("app.urls")),
]
