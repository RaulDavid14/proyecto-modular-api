from rest_framework import serializers
from almacen_app.models.respuestas import RespuestasModel
        

class RespuestasSerializers(serializers.ModelSerializer):
    class Meta:
        model = RespuestasModel
        fields = '__all__' 
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']