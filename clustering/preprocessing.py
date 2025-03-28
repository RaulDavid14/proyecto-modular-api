import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from clustering.models import DatosClustering

def preprocesar_datos(datos, modelo):
    if not datos:
        print("No hay datos para preprocesar")
        return np.array([])

    # Encuentra la longitud de la lista más larga
    max_length = max(len(item) for item in datos)

    # Rellenar las listas más cortas con ceros
    for i in range(len(datos)):
        if len(datos[i]) > max_length:
            datos[i] = datos[i][:max_length]

    datos_np = np.array(datos)
    print("Datos después de hacerlos homogéneos:", datos_np)

    print("Datos antes de escalar:", datos_np)

    # Elegir el tipo de escalado
    if datos_np.shape[0] > 1:
        scaler = StandardScaler()
        scaler_name = 'StandardScaler'
    else:
        scaler = MinMaxScaler()
        scaler_name = 'MinMaxScaler'

    # Escalar los datos
    datos_escalados = scaler.fit_transform(datos_np)
    print("Datos escalados:", datos_escalados)

    # Actualizar los datos en el modelo
    datos_clustering = DatosClustering.objects.filter(modelo=modelo).last()
    if datos_clustering:
        datos_clustering.datos_preprocesados = datos_escalados.tolist()
        datos_clustering.scaler_utilizado = scaler_name
        datos_clustering.save()

    return datos_escalados

def limpiar_datos(datos):
    if not datos:
        print("No hay datos para limpiar")
        return []

    # Convertir a NumPy array para facilitar el manejo
    datos_np = np.array(datos, dtype=np.float64)

    # Eliminar filas con valores NaN o infinitos
    datos_np = datos_np[~np.isnan(datos_np).any(axis=1)]
    datos_np = datos_np[~np.isinf(datos_np).any(axis=1)]

    print("Datos después de la limpieza:", datos_np)

    return datos_np.tolist()  
