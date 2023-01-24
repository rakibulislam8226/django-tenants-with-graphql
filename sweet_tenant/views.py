from django.views.generic import ListView
from django.shortcuts import render
from . models import Sweet
# Create your views here.
class Index(ListView):
    model = Sweet
    template_name = 'sweet_tenant/index.html'
    context_object_name = "Sweet"


# rest framework start #
from .models import Sweet
from .serializers import SweetSerializer
from rest_framework import generics

class SweetList(generics.ListCreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer

class SweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
 # rest framework end #