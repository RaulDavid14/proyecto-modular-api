from django.db import models

class ProgresoUsuarioModel(models.Model):
    id_usuario = models.IntegerField()
    progreso = models.JSONField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'progreso_usuario'
        verbose_name = 'progreso usuario'
        verbose_name_plural = 'progresos de usuario'
        
    def __str__(self):
        return f'Progreso del usuario {self.id_usuario}'