from rest_framework import serializers
from .models import Quarto
from categoriaquarto.serializer import CategoriaquartoSerializer

class QuartoSerializer(serializers.ModelSerializer):
    categoriaquarto = CategoriaquartoSerializer()

    class Meta:
        model = Quarto
        fields = '__all__'