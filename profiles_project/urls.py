from django.contrib import admin
from django.urls import path, include
# import profiles_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls')),
]
