from .models import Reserva
from cliente.serializer import ClienteSerializer
from servicoadicional.serializer import ServicoadicionalSerializer
from quarto.serializer import QuartoSerializer
from rest_framework import serializers


class ReservaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    servicoadicional = ServicoadicionalSerializer()
    quarto = QuartoSerializer()

    
    class Meta:
        model = Reserva
        fields = '__all__'