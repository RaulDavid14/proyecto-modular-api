
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clustering/', include('clustering.urls')),
    path('api/almacen/', include('almacen_app.api.urls')),
    path('api/respuestas/', include('respuestas_app.api.urls')),
]

