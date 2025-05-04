from django.urls import path
from respuestas_app.api.views.respuesta import (
    CreateRespuestaView
    ,RetrieveRespuestaView
    ,DestroyRespuestaView
)
from respuestas_app.api.views.progreso import (
    CreateProgresoView
)

from respuestas_app.api.views.datos_generales import (
    CDatosGeneralesAV
    ,RUDDatosGeneralesAV
)

urlpatterns = [
    path('crear/', CreateRespuestaView.as_view(), name='crear_respuesta'),
    path('detail/<int:id_usuario>/<int:id_cuestionario>', RetrieveRespuestaView.as_view(), name='ver_respuesta'),
    path('delete/<int:id_usuario>/<int:id_cuestionario>/<str:cuestionario>', DestroyRespuestaView.as_view(), name='delete_respuesta'),
    
    path('crear/progreso/', CreateProgresoView.as_view(), name='crear_progreso'),
    
    path('guardar/datosgenerales', CDatosGeneralesAV.as_view(), name='crear_datos_generales'),
    path('datosgenerales/<int:usuario>', RUDDatosGeneralesAV.as_view(), name='datos_generales'),
]