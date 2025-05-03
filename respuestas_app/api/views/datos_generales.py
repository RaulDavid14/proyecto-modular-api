from rest_framework import generics
from respuestas_app.api.serializers.datos_generales import DatosGeneralesSerializer
from respuestas_app.models.datos_generales import DatosGeneralesModel



class CDatosGeneralesAV(generics.CreateAPIView):
    queryset = DatosGeneralesModel.objects.all()
    serializer_class = DatosGeneralesSerializer

class RDatosGeneralesAV(generics.RetrieveAPIView):
    queryset = DatosGeneralesModel.objects.all()
    serializer_class = DatosGeneralesSerializer
    
class UDatosGeneralesAV(generics.UpdateAPIView):
    queryset = DatosGeneralesModel.objects.all()
    serializer_class = DatosGeneralesSerializer

class DDAtosGeneralesAV(generics.DestroyAPIView):
    queryset = DatosGeneralesModel.objects.all()
    

class RUDDatosGeneralesAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatosGeneralesModel.objects.all()
    serializer_class = DatosGeneralesSerializer
    lookup_field = 'usuario'