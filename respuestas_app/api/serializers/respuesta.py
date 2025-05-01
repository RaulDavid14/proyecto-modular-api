from rest_framework import serializers
from respuestas_app.models.respuesta import RespuestaModel

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaModel
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']