from .views import CreateOneObject, ViewOneObject
from django.urls import path, re_path

urlpatterns = [
    path('/<int:id>', ViewOneObject.as_view()),
    path('/creation', CreateOneObject.as_view()),
]