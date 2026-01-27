"""URL Configuration for Django Async Project"""
from django.urls import path, include

# Main URL patterns
urlpatterns = [
    path('', include('asyncviews.urls')),
]