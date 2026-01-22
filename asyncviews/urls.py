from django.urls import path
from .views import async_view, sync_view

urlpatterns = [
    path('async-counter/', async_view, name='async_counter'),
    path('sync-counter/', sync_view, name='sync_counter'),
]