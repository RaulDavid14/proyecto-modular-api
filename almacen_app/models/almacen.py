from django.db import models

#Modelo que va utilizar el clustering para mostrar los resultados

class AlmacenModel(models.Model):
    id_usuario = models.IntegerField(verbose_name='usuario')
    id_cuestionario = models.IntegerField('cuestionario')
    no_pregunta = models.IntegerField('no. pregunta')
    id_respuesta = models.IntegerField('respuesta')
    id_poblacion = models.IntegerField()
    id_sexo = models.IntegerField()
    id_nivel_educativo = models.IntegerField()
    id_ingresos = models.IntegerField()
    id_situacion_laboral = models.IntegerField()
    
    class Meta:
        db_table = 'respuestas_dw'
        verbose_name = 'respuesta almacen'
        verbose_name_plural = 'respuestas almacen'
        