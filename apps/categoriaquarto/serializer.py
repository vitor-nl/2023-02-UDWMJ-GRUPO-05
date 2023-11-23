from .models import Categoriaquarto
from rest_framework import serializers

class CategoriaquartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoriaquarto
        fields = '__all__'