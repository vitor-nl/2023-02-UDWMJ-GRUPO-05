from django.shortcuts import render
from .models import Servicoadicional
from rest_framework import viewsets
from .serializer import ServicoadicionalSerializer

class ServicoadicionalViewSet(viewsets.ModelViewSet):
    queryset = Servicoadicional.objects.all()
    serializer_class = ServicoadicionalSerializer 