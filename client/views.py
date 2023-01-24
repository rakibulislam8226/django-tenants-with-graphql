from django.shortcuts import render
from client.models import Client
from client.serializers import ClientSerializer
# Create your views here.


# rest framework start #
from .models import Client
from .serializers import ClientSerializer
from rest_framework import generics


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
 # rest framework end #