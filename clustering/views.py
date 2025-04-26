from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .clustering import guardar_resultados
from rest_framework.views import APIView
from rest_framework.response import Response
from almacen_app.models.serializers import ResultadoClusteringSerializer

class ClusteringView(View):
    def get(self, request):
        resultados = guardar_resultados()
        return JsonResponse(resultados)

def clustering_template(request):
    resultados = guardar_resultados()
    return render(request, "clustering/clustering_results.html", {"resultados": resultados})

class ClusteringAPIView(APIView):
    def get(self, request):
        resultados = guardar_resultados()
        if 'clustering' in resultados:
            serializer = ResultadoClusteringSerializer(data=resultados['clustering'], many=True)
            serializer.is_valid(raise_exception=True)
            return Response({'clustering': serializer.data})
        return Response(resultados)
