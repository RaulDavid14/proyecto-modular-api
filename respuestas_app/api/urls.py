from django.urls import path
from respuestas_app.api.views.respuesta import (
    CreateRespuestaView
    ,RetrieveRespuestaView
    ,DestroyRespuestaView
)
from respuestas_app.api.views.progreso import (
    CreateProgresoView
)

urlpatterns = [
    path('crear/', CreateRespuestaView.as_view(), name='crear_respuesta'),
    path('detail/<int:id_usuario>/<int:id_cuestionario>', RetrieveRespuestaView.as_view(), name='ver_respuesta'),
    path('delete/<int:id_usuario>/<str:cuestionario>', DestroyRespuestaView.as_view(), name='delete_respuesta'),
    
    path('crear/progreso/', CreateProgresoView.as_view(), name='crear_progreso'),
]