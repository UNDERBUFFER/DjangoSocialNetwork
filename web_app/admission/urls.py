from .views import *
from django.urls import path

urlpatterns = [
    path('/registration', registration),
    path('/entrance', entrance),
]