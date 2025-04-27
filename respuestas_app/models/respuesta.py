from django.db import models
from respuestas_app.managers.respuesta import RespuestaManager

class RespuestaModel(models.Model):
    id_usuario = models.IntegerField()
    respuestas = models.JSONField()
    id_cuestionario = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    objects = RespuestaManager()
    
    class Meta:
        db_table = 'respuestas'
        verbose_name = 'respuesta'
        verbose_name_plural = 'respuestas'