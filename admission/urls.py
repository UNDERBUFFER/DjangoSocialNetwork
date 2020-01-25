from .views import choice, entrance, registration
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', choice),
    path('/entrance', entrance, name='ent'),
    path('/registration', registration, name='reg'),
]