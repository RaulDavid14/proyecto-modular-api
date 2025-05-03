from rest_framework import serializers

class ResultadoClusteringSerializer(serializers.Serializer):
    id_usuario = serializers.IntegerField()
    id_poblacion = serializers.IntegerField()
    id_sexo = serializers.IntegerField()
    id_nivel_educativo = serializers.IntegerField()
    cluster = serializers.CharField()
