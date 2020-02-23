from .views import chat, settings
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path('/chat', chat, name='chat'),
    path('/settings', settings, name='set'),
]