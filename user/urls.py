from .views import all_walls, wall
from admission.views import not_found
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('/all_walls', all_walls, name='all_walls'),    
    path('/wall/<int:iden>', wall, name='wall'),
    re_path(r'^.+$', not_found),
]