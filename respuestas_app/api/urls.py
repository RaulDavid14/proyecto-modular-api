from django.urls import path
from respuestas_app.api.views.respuesta import (
    CreateRespuestaView
    ,RetrieveRespuestaView
    ,UpdateRespuestaView
    ,DestroyRespuestaView
)

urlpatterns = [
    path('create/', CreateRespuestaView.as_view(), name='crear_respuesta'),
    path('detail/<int:id_usuario>', RetrieveRespuestaView.as_view(), name='ver_respuesta'),
    path('update/<int:id_usuario>', UpdateRespuestaView.as_view(), name='update_respuesta'),
    path('delete/<int:id_usuario>', DestroyRespuestaView.as_view(), name='delete_respuesta'),
]
