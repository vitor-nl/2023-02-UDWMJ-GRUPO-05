from django.shortcuts import render

# Create your views here.
from reserva.models import Reserva
from rest_framework import viewsets
from reserva.serializer import ReservaSerializer
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer