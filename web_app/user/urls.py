from .views import *
from django.urls import path

urlpatterns = [
    path('/<int:id>', User.as_view()),
    path('/<int:author_id>/records', Record.as_view()),
    path('/<int:author_id>/photos', Photo.as_view()),
]
