from django.shortcuts import render
from .models import Categoriaquarto
from rest_framework import viewsets
from .serializer import CategoriaquartoSerializer

# Create your views here.

class CategoriaquartoViewSet(viewsets.ModelViewSet):
    queryset = Categoriaquarto.objects.all()
    serializer_class = CategoriaquartoSerializer 
