from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('medspa.urls')),
    path('api/v1/', include('services.urls')),
    path('api/v1/', include('appointment.urls')),
]


