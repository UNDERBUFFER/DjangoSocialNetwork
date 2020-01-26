from .views import choice, entrance, not_found, registration
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('', choice),
    path('/entrance', entrance, name='ent'),
    path('/registration', registration, name='reg'),
    re_path(r'^.+$', not_found),
]