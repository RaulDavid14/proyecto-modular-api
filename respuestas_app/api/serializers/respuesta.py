from rest_framework import serializers
from respuestas_app.models.respuesta import RespuestaModel

class RespuestaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    id_usuario = serializers.IntegerField()
    abreviacion = serializers.CharField(max_length=5, write_only=True)
    respuestas = serializers.JSONField()
    id_cuestionario = serializers.IntegerField()
    fecha_creacion = serializers.DateTimeField(read_only = True)
    fecha_actualizacion = serializers.DateTimeField(read_only = True)
    
    def create(self, validated_data):
        # Quitar "abreviacion" porque no es parte del modelo
        abreviacion = validated_data.pop('abreviacion', None)
        return RespuestaModel.objects.create(**validated_data)