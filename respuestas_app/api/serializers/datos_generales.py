from rest_framework import serializers
from respuestas_app.models.datos_generales import DatosGeneralesModel

class DatosGeneralesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DatosGeneralesModel
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']