import numpy as np
from sklearn.cluster import KMeans
from .data_extraction import obtener_datos_usuarios
from .preprocessing import preprocesar_datos, limpiar_datos
from almacen_app.models import AlmacenModel

def aplicar_clustering():
    try:
        datos = obtener_datos_usuarios()
        datos_procesados = preprocesar_datos(datos)
        datos_limpios = limpiar_datos(datos)

        if datos_procesados.size == 0:
            return {"error": "No hay suficientes datos para clustering"}

        modelo = KMeans(n_clusters=4, random_state=42)
        modelo.fit(datos_procesados)
        etiquetas = modelo.labels_.tolist()

        niveles_consumo = {0: "Bajo", 1: "Moderado", 2: "Normal", 3: "Excesivo"}

        usuarios = AlmacenModel.objects.values(
            'id_usuario', 'id_poblacion', 'id_sexo', 'id_nivel_educativo'
        ).distinct().order_by('id_usuario')

        usuarios = list(usuarios)

        resultados = []
        for i, usuario in enumerate(usuarios):
            nivel_consumo = niveles_consumo.get(etiquetas[i], "Desconocido")

            resultados.append({
                "id_usuario": usuario['id_usuario'],
                "id_poblacion": usuario['id_poblacion'],
                "id_sexo": usuario['id_sexo'],
                "id_nivel_educativo": usuario['id_nivel_educativo'],
                "cluster": nivel_consumo
            })

        return {"clustering": resultados}

    except Exception as e:
        return {"error": str(e)}

def guardar_resultados():
    return aplicar_clustering()
