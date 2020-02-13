from .views import ViewOneObject
from django.urls import path, re_path

urlpatterns = [
    path('/<int:iden>', ViewOneObject.as_view()),
]