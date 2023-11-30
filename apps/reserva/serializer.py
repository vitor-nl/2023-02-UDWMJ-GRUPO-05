from .models import Reserva
from rest_framework import serializers
from quarto.serializer import QuartoSerializer
from cliente.serializer import ClienteSerializer
from servicoadicional.serializer import ServicoadicionalSerializer

class ReservaSerializer(serializers.ModelSerializer):
    quarto = QuartoSerializer()
    cliente = ClienteSerializer()
    servicoadicional = ServicoadicionalSerializer()

    class Meta:
        model = Reserva
        fields = '__all__'