from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('/<int:id>', User.as_view()),
    path('/<int:author_id>/records', Record.as_view()),
    path('/<int:author_id>/photos', Photo.as_view()),
]