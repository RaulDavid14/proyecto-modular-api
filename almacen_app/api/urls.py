from django.urls import path
from .views import *

urlpatterns = [
    path('total', get_total, name='total'),
]
