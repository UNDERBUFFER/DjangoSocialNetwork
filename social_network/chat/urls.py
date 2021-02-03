from .views import Message, Ignore
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('/chat', Message.as_view()),
    path('/ignore', Ignore.as_view()),
]
