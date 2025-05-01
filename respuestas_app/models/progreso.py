from django.db import models
from respuestas_app.managers.progreso import ProgresoManager
from clients.clients import Clientes

class ProgresoModel(models.Model):
    id_usuario = models.IntegerField()
    progreso = models.JSONField()
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    objects = ProgresoManager()
    
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.progreso = self.create_progreso()
        
        return super(ProgresoModel, self).save(*args, **kwargs)
    
    def create_progreso(self):
        progreso = {}
        response = Clientes.get_cuestionarios()
        
        for cuestionario in response:
            progreso[cuestionario['abreviacion']] = {
                'completo' : False
            }
            
        return progreso
    
    class Meta:
        #aqui se muestra como ordenar los campos de un modelo
        db_table = 'progreso_usuario'
        verbose_name = 'progreso'
        verbose_name_plural = 'progresos'
        