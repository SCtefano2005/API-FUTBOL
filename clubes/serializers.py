from rest_framework import serializers
from .models import *

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        
class ClubDetailSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()  # Anidamos

    class Meta:
        model = Club
        fields = '__all__'

class ClubCreateSerializer(serializers.ModelSerializer):
    departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())  # Solo el ID para escritura

    class Meta:
        model = Club
        fields = '__all__'