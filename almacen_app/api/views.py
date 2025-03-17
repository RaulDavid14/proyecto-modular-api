from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from clients.clients import Clientes

@api_view()
def get_total(request):
    cantidad = Clientes.obtener_total_preguntas()
    data = {
        'total' : cantidad['total']
    }
    
    return Response(data, status=status.HTTP_200_OK)