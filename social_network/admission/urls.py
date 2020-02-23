from .views import *
from django.urls import path

urlpatterns = [
    path('/registration', Admission.as_view(act='registration')),
    path('/entrance', Admission.as_view(act='entrance')),
]