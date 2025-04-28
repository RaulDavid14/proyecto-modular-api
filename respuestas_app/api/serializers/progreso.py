from rest_framework import serializers
from respuestas_app.models.progreso import ProgresoModel

class ProgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoModel
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']