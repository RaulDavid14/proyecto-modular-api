from almacen_app.models.progreso import ProgresoUsuarioModel as Progreso
from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework import status
from .serializers.respuestas_serializers import RespuestasSerializers

class CreateRespuestasAV(APIView):
    def post(self, request):
        serializer = RespuestasSerializers(data = request.data)
        
        if serializer.is_valid():
            progreso = Progreso()
            id_usuario = request.data.get('id_usuario')
            id_cuestionario = request.data.get('id_cuestionario')
            
            
                            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        