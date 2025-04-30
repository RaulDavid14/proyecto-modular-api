from django.db import models

class ProgresoManager(models.Manager):
    
    def getProgreso(self, id_usuario):
        return self.filter(id_usuario = id_usuario)