from .models import Reserva
from cliente.serializer import ClienteSerializer
from quarto.serializer import QuartoSerializer
from rest_framework import serializers
from quarto.serializer import QuartoSerializer
from cliente.serializer import ClienteSerializer



class ReservaSerializer(serializers.ModelSerializer):
    quarto = QuartoSerializer()
    cliente = ClienteSerializer()

    class Meta:
        model = Reserva
        fields = '__all__'