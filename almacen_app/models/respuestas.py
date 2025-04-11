from django.db import models

"""
    este modelo guarda las respuestas del usuario una vez que ccompleto un
    cuestionario, para controlar en caso de que el usuario reinicie el cuestionario
    y solo mandar al almacen respuestas completas. 
"""

class RespuestasModel(models.Model):
    id_usuario = models.IntegerField(verbose_name='id usuario')
    id_cuestionario = models.IntegerField(verbose_name='id del cuestionario')
    respuestas = models.JSONField('respuestas usuario')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'respuestas_usuario'
        verbose_name = 'Respuesta del usuario'
        verbose_name_plural = 'Respuestas de los usuarios'
        
    def __str__(self):
        return f'Respuesta de usuario {self.id_usuario}'
    
