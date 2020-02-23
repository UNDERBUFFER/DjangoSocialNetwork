from .views import *
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path('/registration', Admission.as_view(act='registration')),
    path('/entrance', Admission.as_view(act='entrance')),
]