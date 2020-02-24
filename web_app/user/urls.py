from .views import *
from django.urls import path

urlpatterns = [
    path('/<int:id>', lambda: None),
    path('/<int:author_id>/records', lambda: None),
    path('/<int:author_id>/photos', lambda: None),
]