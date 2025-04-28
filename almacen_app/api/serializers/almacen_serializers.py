from rest_framework.serializers import ModelSerializer
from almacen_app.models.almacen import AlmacenModel

class AlmacenSerializers(ModelSerializer):
    class Meta:
        model = AlmacenModel
        fields = ['__all__']