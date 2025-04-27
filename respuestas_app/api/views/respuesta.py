from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from respuestas_app.models.respuesta import RespuestaModel
from respuestas_app.api.serializers.respuesta import RespuestaSerializer
from django.shortcuts import get_object_or_404


class CreateRespuestaView(CreateAPIView):
    queryset = RespuestaModel.objects.all()
    serializer_class = RespuestaSerializer

class RetrieveRespuestaView(RetrieveAPIView):
    queryset = RespuestaModel.objects.all()
    serializer_class = RespuestaSerializer

    def get_object(self):
        id_usuario = self.kwargs.get('id_usuario')
        respuesta = get_object_or_404(RespuestaModel, id_usuario=id_usuario)
        return respuesta

class UpdateRespuestaView(UpdateAPIView):
    queryset = RespuestaModel.objects.all()
    serializer_class = RespuestaSerializer
    
class DestroyRespuestaView(DestroyAPIView):
    queryset = RespuestaModel.objects.all()
    serializer_class = RespuestaSerializer