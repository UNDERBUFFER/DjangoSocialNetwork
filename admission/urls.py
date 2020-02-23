from .views import *
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path('/admission/registration', Admission.as_view(act='registration')),
    path('/admission/entrance', Admission.as_view(act='entrance')),
]