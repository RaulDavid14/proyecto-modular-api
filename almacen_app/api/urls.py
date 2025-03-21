from django.urls import path
from .views import *

urlpatterns = [
    path('total', get_total, name='total'),
    path('datos-generales', add_datos_generales, name='add_datos_generales'),
]
