from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView
from respuestas_app.models.respuesta import RespuestaModel
from respuestas_app.api.serializers.respuesta import RespuestaSerializer
from django.shortcuts import get_object_or_404
from respuestas_app.models.progreso import ProgresoModel
from rest_framework.response import Response
from rest_framework import status

class CreateRespuestaView(CreateAPIView):
    queryset = RespuestaModel.objects.all()
    serializer_class = RespuestaSerializer

    def perform_create(self, serializer):
        datos = serializer.validated_data

        id_usuario = datos['id_usuario']
        id_cuestionario = datos['id_cuestionario']

        serializer.save()

        progreso_obj, creado = ProgresoModel.objects.get_or_create(id_usuario=id_usuario)

        progreso = progreso_obj.progreso

        if id_cuestionario in progreso:
            progreso[id_cuestionario]['completo'] = True
        else:
            progreso[id_cuestionario] = {'completo': True}

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
        
        respuesta = self.get_object()

        id_usuario = respuesta.id_usuario
        id_cuestionario = respuesta.id_cuestionario  

        try:
            progreso_obj = ProgresoModel.objects.get(id_usuario=id_usuario)
            progreso = progreso_obj.progreso

            if id_cuestionario in progreso:
                progreso[id_cuestionario]['completo'] = False
                progreso_obj.progreso = progreso
                progreso_obj.save(update_fields=['progreso', 'fecha_actualizacion'])
        except ProgresoModel.DoesNotExist:
            pass  

        
        respuesta.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
