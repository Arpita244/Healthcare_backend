"""
Main URL configuration for the Healthcare project.
Routes admin and API endpoints to their respective modules.
"""
from django.contrib import admin
from django.urls import path, include

# URL patterns for the project
urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    # API endpoints
    path('api/', include('api.urls')),
]
