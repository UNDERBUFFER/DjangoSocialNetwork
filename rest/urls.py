from .views import AuthView, GetPostRecord, GetUser, PostUser, Home
from django.urls import path, re_path

urlpatterns = [
    path('/<int:id>', GetUser.as_view()),
    path('/<int:author_id>/records', GetPostRecord.as_view()),
    path('/creation', PostUser.as_view()),
    path('/auth', AuthView.as_view()),
    path('/home', Home.as_view()),
]