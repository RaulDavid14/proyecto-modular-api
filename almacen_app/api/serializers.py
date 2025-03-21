from rest_framework import serializers

class DatosgeneralesSerializer(serializers.Serializer):
    usuario = serializers.IntegerField()
    poblacion = serializers.IntegerField()
    sexo = serializers.IntegerField()
    nivel_educativo = serializers.IntegerField()
    
