import numpy as np
from sklearn.cluster import KMeans
from .data_extraction import obtener_datos_usuarios
from .preprocessing import preprocesar_datos, limpiar_datos
from catalogos.models import DatosGenerales
from clustering.models import ModeloClustering, ResultadoClustering

def aplicar_clustering(modelo_nombre="Modelo Predeterminado"):
    try:
        # Obtener los datos de usuarios y el modelo
        datos, modelo = obtener_datos_usuarios(modelo_nombre)
        print("Datos obtenidos:", datos)

        # Preprocesar los datos
        datos_procesados = preprocesar_datos(datos, modelo)
        print("Datos procesados:", datos_procesados)

        # Limpiar los datos
        datos_limpios = limpiar_datos(datos)
        print("Datos limpios:", datos_limpios)

        if datos_procesados.size == 0:
            print("No hay datos suficientes para clustering")
            return {"error": "No hay suficientes datos para clustering"}

        # Crear el modelo de clustering (KMeans)
        kmeans = KMeans(n_clusters=modelo.num_clusters, random_state=modelo.random_state)
        kmeans.fit(datos_procesados)

        # Guardar los parámetros del modelo
        modelo.parametros = {
            'inertia': float(kmeans.inertia_),
            'n_iter': int(kmeans.n_iter_),
            'cluster_centers': kmeans.cluster_centers_.tolist()
        }
        modelo.save()

        # Obtener las etiquetas de los clusters
        etiquetas = kmeans.labels_.tolist()
        print("Etiquetas de los clusters:", etiquetas)

        # Definir los niveles de consumo
        niveles_consumo = {0: "Bajo", 1: "Moderado", 2: "Normal", 3: "Excesivo"}

        # Obtener los usuarios de la base de datos
        usuarios = DatosGenerales.objects.all()
        print("Usuarios obtenidos:", list(usuarios))

        # Guardar los resultados de clustering en la base de datos
        resultados_db = []
        resultados_api = []
        
        for i, usuario in enumerate(usuarios):
            nivel_consumo = niveles_consumo.get(etiquetas[i], "Desconocido")
            
            # Crear o actualizar resultado en la base de datos
            resultado, created = ResultadoClustering.objects.update_or_create(
                modelo=modelo,
                usuario=usuario,
                defaults={
                    'cluster_asignado': etiquetas[i],
                    'nivel_consumo': nivel_consumo,
                    # Puedes calcular la distancia al centroide si es necesario
                }
            )
            resultados_db.append(resultado)
            
            # Preparar respuesta para la API
            resultados_api.append({
                "user_id": usuario.id,
                "sexo_id": usuario.sexo.id if usuario.sexo else "Desconocido",
                "poblacion_id": usuario.poblacion.id if usuario.poblacion else "Desconocido",
                "nivel_educativo_id": usuario.nivel_educativo.id if usuario.nivel_educativo else "Desconocido",
                "cluster": nivel_consumo,
                "cluster_num": etiquetas[i]
            })

        print("Resultados de clustering guardados:", len(resultados_db))
        return {
            "clustering": resultados_api,
            "modelo_id": modelo.id,
            "modelo_nombre": modelo.nombre,
            "num_clusters": modelo.num_clusters
        }
    
    except Exception as e:
        print("Error en aplicar_clustering:", e)
        return {"error": str(e)}

def guardar_resultados():
    return aplicar_clustering()