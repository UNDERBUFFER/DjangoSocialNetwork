from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('/admission/registration', Admission.as_view(act='registration')),
    path('/admission/entrance', Admission.as_view(act='entrance')),
    path('/user/<int:id>', User.as_view()),
    path('/user/<int:author_id>/records', Record.as_view()),
    path('/user/<int:id>/photos', lambda: None),
    path('/chat/chat', lambda: None),
    path('/chat/settings', lambda: None),
]