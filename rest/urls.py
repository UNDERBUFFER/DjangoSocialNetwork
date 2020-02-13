from .views import ViewOneObject, ViewCreateObject
from django.urls import path, re_path

urlpatterns = [
    path('/<int:iden>', ViewOneObject.as_view()),
    path('/create', ViewCreateObject.as_view()),
]