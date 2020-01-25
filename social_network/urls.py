from admission.views import start
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start),
    path('admission', include('admission.urls')),
    path('user', include('user.urls'))
]
