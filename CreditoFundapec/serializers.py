from rest_framework import serializers
from .models import Transaccion, Estudiante


class CreditoSerializer(serializers.Serializer):
    monto = serializers.DecimalField(decimal_places=2, max_digits=10)
    id = serializers.ReadOnlyField()


class EstudianteSerializer(serializers.Serializer):
    credito = CreditoSerializer()
    nombre = serializers.CharField(max_length=150)
    apellidos = serializers.CharField(max_length=150)
    matricula = serializers.CharField(max_length=150)


class TransaccionSerilizer(serializers.Serializer):
    monto = serializers.DecimalField(decimal_places=2, max_digits=10)
    matricula = serializers.CharField(max_length=8, source='credito.estudiante.matricula')

    def create(self, validated_data):
        print(validated_data)
        credito = validated_data.pop('credito')
        estudiante = Estudiante.objects.get(matricula=credito['estudiante']['matricula'])
        validated_data.update(credito_id=estudiante.credito.pk)
        return Transaccion.objects.create(**validated_data)
