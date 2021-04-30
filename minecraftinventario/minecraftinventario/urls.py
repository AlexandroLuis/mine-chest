from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    # User Management
    path("accounts/", include("allauth.urls")),
    # Local
    path("", include("pages.urls", namespace="pages")),
]
