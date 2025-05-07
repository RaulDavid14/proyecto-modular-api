import numpy as np
from sklearn.cluster import KMeans
from .data_extraction import obtener_datos_usuarios
from .preprocessing import preprocesar_datos, limpiar_datos
from almacen_app.models import AlmacenModel

def aplicar_clustering():
    try:
        # Obtener datos de usuarios
        datos = obtener_datos_usuarios()
        print(f"Datos obtenidos: {len(datos)}")  # Ver cuántos datos se han obtenido

        # Limpiar y procesar los datos
        datos_limpios = limpiar_datos(datos)
        datos_procesados = preprocesar_datos(datos_limpios)

        if datos_procesados.size == 0:
            return {"error": "No hay suficientes datos para clustering"}

        # Aplicar KMeans clustering
        modelo = KMeans(n_clusters=4, random_state=42)
        modelo.fit(datos_procesados)
        etiquetas = modelo.labels_.tolist()

        print(f"Etiquetas generadas: {etiquetas}")  # Ver cuántas etiquetas se generaron

        # Verificar que las etiquetas y los usuarios coincidan
        if len(etiquetas) != len(datos_procesados):
            print(f"Error: número de etiquetas ({len(etiquetas)}) no coincide con el número de datos procesados ({len(datos_procesados)})")
            return {"error": "Mismatch en la cantidad de etiquetas y datos"}

        # Mapear las etiquetas de clusters a niveles de consumo
        niveles_consumo = {0: "Bajo", 1: "Moderado", 2: "Normal", 3: "Excesivo"}

        # Obtener usuarios de la base de datos
        usuarios = AlmacenModel.objects.values(
            'id_usuario', 'id_poblacion', 'id_sexo', 'id_nivel_educativo'
        ).distinct().order_by('id_usuario')

        usuarios = list(usuarios)

        print(f"Usuarios obtenidos: {len(usuarios)}")  # Ver cuántos usuarios se recuperaron

        # Crear resultados con los clusters asignados a los usuarios
        resultados = []
        for i, usuario in enumerate(usuarios):
            if i >= len(etiquetas):  # Verificar que el índice esté dentro de los límites
                print(f"Índice fuera de rango: {i}")
                break
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
        print(f"Error en aplicar_clustering: {str(e)}")
        return {"error": str(e)}

def guardar_resultados():
    return aplicar_clustering()
