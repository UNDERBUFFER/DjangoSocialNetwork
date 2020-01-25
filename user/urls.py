from django.contrib import admin
from django.urls import include, path
from .views import all_pages, page

urlpatterns = [
    path('/all_pages', all_pages, name='all_pages'),    
    path('/page/<int:iden>', page, name='page'),
]