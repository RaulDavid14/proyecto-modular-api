from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from respuestas_app.models.progreso import ProgresoModel
from respuestas_app.api.serializers.progreso import ProgresoSerializer 

class CreateRespuestaView(CreateAPIView):
    queryset = ProgresoModel.objects.all()
    serializer_class = ProgresoSerializer

