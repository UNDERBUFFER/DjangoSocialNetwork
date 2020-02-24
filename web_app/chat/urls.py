from .views import *
from django.urls import path

urlpatterns = [
    path('/chat', lambda: None),
    path('/ignore', lambda: None),
]