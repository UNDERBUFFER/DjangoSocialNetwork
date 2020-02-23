from .views import *
from django.urls import path

urlpatterns = [
    path('/chat/chat', lambda: None),
    path('/chat/settings', lambda: None),
]