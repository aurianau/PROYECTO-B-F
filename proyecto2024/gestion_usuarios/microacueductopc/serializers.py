from rest_framework import serializers
from .models import Vivienda

class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vivienda
        fields = ['id', 'numero_habitantes', 'propietario', 'direccion', 'telefono']
