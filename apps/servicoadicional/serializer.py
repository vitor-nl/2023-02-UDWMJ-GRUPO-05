from rest_framework import serializers
from .models import Servicoadicional

class ServicoadicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicoadicional
        fields = '__all__'