from rest_framework import generics
from .models import MedSpa
from .serializers import MedSpaSerializer

class MedSpaListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedSpa.objects.all()
    serializer_class = MedSpaSerializer

class MedSpaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedSpa.objects.all()
    serializer_class = MedSpaSerializer
