from django.shortcuts import render

# Create your views here.
# rest framework start #
from .models import SweetType
from .serializers import SweetTypeSerializer
from rest_framework import generics

class SweetSharedList(generics.ListCreateAPIView):
    queryset = SweetType.objects.all()
    serializer_class = SweetTypeSerializer

class SweetSharedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SweetType.objects.all()
    serializer_class = SweetTypeSerializer
 # rest framework end #