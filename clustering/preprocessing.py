import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def preprocesar_datos(datos):
    if not datos:
        return np.array([])

    max_length = max(len(item) for item in datos)

    for i in range(len(datos)):
        if len(datos[i]) > max_length:
            datos[i] = datos[i][:max_length]

    datos_np = np.array(datos)

    scaler = StandardScaler() if datos_np.shape[0] > 1 else MinMaxScaler()
    datos_escalados = scaler.fit_transform(datos_np)

    return datos_escalados

def limpiar_datos(datos):
    if not datos:
        return []

    datos_np = np.array(datos, dtype=np.float64)
    datos_np = datos_np[~np.isnan(datos_np).any(axis=1)]
    datos_np = datos_np[~np.isinf(datos_np).any(axis=1)]

    return datos_np.tolist()
