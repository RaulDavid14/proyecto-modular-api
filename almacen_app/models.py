from django.db import models

class RespuestaModel(models.Model):
    
    class Meta:
        db_table = 'respuestas'
        verbose_name = 'respuesta'
        verbose_name_plural = 'repsuestas'

class DatosGeneralesModel(models.Model):
    
    class Meta:
        db_table = 'datos_generales_usuario'
        verbose_name = 'datos generales del usuario'
        verbose_name_plural = 'listado de datos generales'


class AlmacenModel(models.Model):
    id_usuario = models.IntegerField(verbose_name='usuario')
    id_cuestionario = models.IntegerField('cuestionario')
    no_pregunta = models.IntegerField('no. pregunta')
    id_respuesta = models.IntegerField('respuesta')
    """
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
        poblacion = models.ForeignKey(CatPoblacion, on_delete=models.CASCADE, verbose_name="Población")
        sexo = models.ForeignKey(CatSexo, on_delete=models.CASCADE, verbose_name="Sexo")
        nivel_educativo = models.ForeignKey(CatNivelEducativo, on_delete=models.CASCADE, verbose_name="Nivel Educativo")
    """    
    
    id_poblacion = models.IntegerField()
    id_sexo = models.IntegerField()
    id_nivel_educativo = models.IntegerField()
    id_ingresos = models.IntegerField()
    id_situacion_laboral = models.IntegerField()
    
    class Meta:
        db_table = 'respuestas_dw'
        verbose_name = 'respuesta almacen'
        verbose_name_plural = 'respuestas almacen'
        