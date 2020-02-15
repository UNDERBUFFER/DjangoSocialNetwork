from .views import GetPostRecord, GetUser, PostUser
from django.urls import path, re_path

urlpatterns = [
    path('/<int:id>', GetUser.as_view()),
    path('/<int:author_id>/records', GetPostRecord.as_view()),
    path('/creation', PostUser.as_view()),
]