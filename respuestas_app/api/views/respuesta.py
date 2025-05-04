from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView
from respuestas_app.models.respuesta import RespuestaModel
from respuestas_app.api.serializers.respuesta import RespuestaSerializer, CreateRespuestaSerializer
from django.shortcuts import get_object_or_404
from respuestas_app.models.progreso import ProgresoModel
from rest_framework.response import Response
from rest_framework import status

class CreateRespuestaView(CreateAPIView):
    queryset = RespuestaModel.objects.all()
    serializer_class = RespuestaSerializer  # Usa el correcto

    def perform_create(self, serializer):
        # Primero, accedemos al validated_data para extraer los datos necesarios
        abreviacion = serializer.validated_data.get('abreviacion')
        id_usuario = serializer.validated_data.get('id_usuario')
        id_cuestionario = serializer.validated_data.get('id_cuestionario')

        # Guardamos la respuesta (esto ya elimina 'abreviacion' internamente)
        respuesta = serializer.save()

        # Actualizamos el progreso del usuario
        progreso_obj, creado = ProgresoModel.objects.get_or_create(id_usuario=id_usuario)
        progreso = progreso_obj.progreso

        if id_cuestionario in progreso:
            progreso[abreviacion]['completo'] = True
        else:
            progreso[abreviacion] = {'completo': True}

        progreso_obj.progreso = progreso
        progreso_obj.save(update_fields=['progreso', 'fecha_actualizacion'])
    
class RetrieveRespuestaView(RetrieveAPIView):
    queryset = RespuestaModel.objects.all()
    serializer_class = RespuestaSerializer

    def get_object(self):
        id_usuario = self.kwargs.get('id_usuario')
        id_cuestionario = self.kwargs.get('id_cuestionario')
        
        respuesta = get_object_or_404(RespuestaModel, id_usuario=id_usuario, id_cuestionario=id_cuestionario)
        return respuesta

class DestroyRespuestaView(DestroyAPIView):
    queryset = RespuestaModel.objects.all()
    serializer_class = RespuestaSerializer

    def get_object(self):
        id_usuario = self.kwargs.get('id_usuario')
        id_cuestionario = self.kwargs.get('id_cuestionario')

        return get_object_or_404(RespuestaModel, id_usuario=id_usuario, id_cuestionario=id_cuestionario)

    def delete(self, request, *args, **kwargs):
        cuestionario = self.kwargs.get('cuestionario')        
        respuesta = self.get_object()
        id_usuario = respuesta.id_usuario

        try:
            progreso_obj = ProgresoModel.objects.get(id_usuario=id_usuario)
            progreso = progreso_obj.progreso
            if cuestionario in progreso:
                progreso[cuestionario]['completo'] = False
                progreso_obj.progreso = progreso
                progreso_obj.save(update_fields=['progreso', 'fecha_actualizacion'])
        except ProgresoModel.DoesNotExist:
            pass  

        respuesta.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
