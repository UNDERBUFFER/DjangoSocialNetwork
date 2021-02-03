from .views import *
from django.urls import path

urlpatterns = [
    path('/chat', Message.as_view()),
    path('/ignore', Ignore.as_view()),
]
