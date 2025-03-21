from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from clients.clients import Clientes

from .serializers import *

@api_view()
def get_total(request):
    cantidad = Clientes.obtener_total_preguntas()
    data = {
        'total' : cantidad['total']
    }
    
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_datos_generales(request):
    if request.method == 'POST':
        return Response({}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "Método no permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 