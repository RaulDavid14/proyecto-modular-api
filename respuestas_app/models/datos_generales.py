from django.db import models

class DatosGeneralesModel(models.Model):
    usuario = models.IntegerField(unique=True)
    situacion_laboral = models.IntegerField()
    ingresos = models.IntegerField()
    sexo = models.IntegerField()
    poblacion = models.IntegerField()
    nivel_educativo = models.IntegerField()
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'respuestas de {self.usuario}'
    
    class Meta:
        db_table = 'respuestas_datos_generales'
        