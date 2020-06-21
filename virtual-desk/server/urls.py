from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('intro.urls')),
    path('', include('authentication.urls')),
    path('', include('dashboard.urls')),

]
