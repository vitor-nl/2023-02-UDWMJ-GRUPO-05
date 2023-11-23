from django.shortcuts import render

from rest_framework import viewsets
from quarto.models import Quarto
from quarto.serializer import QuartoSerializer

class QuartoViewSet(viewsets.ModelViewSet):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer


