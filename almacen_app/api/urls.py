from django.urls import path
from .views import *

urlpatterns = [
    path('guardar/respuesta', CreateRespuestasAV.as_view(), name='guardar_respuesta')
]
