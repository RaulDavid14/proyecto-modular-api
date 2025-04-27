from django.db import models


class ProgresoModel(models.Model):
    id_usuario = models.IntegerField()
    progreso = models.JSONField()
    
    fecha_reacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        #aqui se muestra como ordenar los campos de un modelo
        db_table = 'progreso_usuario'
        verbose_name = 'progreso'
        verbose_name_plural = 'progresos'
        