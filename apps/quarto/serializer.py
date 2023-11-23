from rest_framework import serializers
from quarto.models import Quarto
from categoriaquarto.serializer import CategoriaquartoSerializer

class QuartoSerializer(serializers.ModelSerializer):
    categoria = CategoriaquartoSerializer()

    class Meta:
        model = Quarto
        fields = 'all'