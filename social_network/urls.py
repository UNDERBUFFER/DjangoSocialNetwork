from admission.views import not_found, start
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start),
    path('admission', include('admission.urls')),
    path('user', include('user.urls')),
    path('chat', include('chat.urls')),
    path('rest', include('rest.urls')),
    re_path(r'^.*$', not_found),
]
