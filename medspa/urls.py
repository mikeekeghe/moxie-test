from django.urls import path
from .views import MedSpaListCreateAPIView, MedSpaRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('medspas/', MedSpaListCreateAPIView.as_view(), name='medspa-list-create'),
    path('medspas/<int:pk>/', MedSpaRetrieveUpdateDestroyAPIView.as_view(), name='medspa-detail'),
]
