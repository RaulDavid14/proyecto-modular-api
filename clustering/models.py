from django.db import models
from catalogos.models import DatosGenerales
from cuestionario.models import PreguntaModel, RespuestaModel

class ModeloClustering(models.Model):
    """
    Modelo principal que almacena la configuración y resultados del clustering
    """
    nombre = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    num_clusters = models.PositiveIntegerField(default=4)
    
    # Parámetros del modelo
    random_state = models.IntegerField(default=42)
    algoritmo = models.CharField(max_length=50, default='KMeans')
    parametros = models.JSONField(default=dict) 
    
    class Meta:
        verbose_name = "Modelo de Clustering"
        verbose_name_plural = "Modelos de Clustering"

    def __str__(self):
        return f"{self.nombre} (Clusters: {self.num_clusters})"

class DatosClustering(models.Model):
    """
    Almacena los datos preprocesados para clustering
    """
    modelo = models.ForeignKey(ModeloClustering, on_delete=models.CASCADE, related_name='datos')
    datos_originales = models.JSONField()  # Datos antes de preprocesamiento
    datos_preprocesados = models.JSONField()  # Datos después de preprocesamiento
    scaler_utilizado = models.CharField(max_length=50)  # Tipo de escalado aplicado
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Datos para Clustering"
        verbose_name_plural = "Datos para Clustering"

class ResultadoClustering(models.Model):
    """
    Almacena los resultados del clustering para cada usuario
    """
    NIVELES_CONSUMO = [
        ('Bajo', 'Bajo'),
        ('Moderado', 'Moderado'),
        ('Normal', 'Normal'),
        ('Excesivo', 'Excesivo'),
        ('Desconocido', 'Desconocido'),
    ]
    
    modelo = models.ForeignKey(ModeloClustering, on_delete=models.CASCADE, related_name='resultados')
    usuario = models.ForeignKey(DatosGenerales, on_delete=models.CASCADE)
    cluster_asignado = models.PositiveIntegerField()
    nivel_consumo = models.CharField(max_length=20, choices=NIVELES_CONSUMO)
    distancia_al_centroide = models.FloatField(null=True, blank=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('modelo', 'usuario')  
        verbose_name = "Resultado de Clustering"
        verbose_name_plural = "Resultados de Clustering"
    
    def __str__(self):
        return f"{self.usuario} - Cluster {self.cluster_asignado} ({self.nivel_consumo})"