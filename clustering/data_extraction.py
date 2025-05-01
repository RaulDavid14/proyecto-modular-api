
from almacen_app.models import AlmacenModel

#from almacen_app.models import DatosGeneralesModel, RespuestaModel
from clients.clients import Clientes
from collections import defaultdict

def obtener_datos_usuarios():
    datos = []
    respuestas_por_usuario = defaultdict(list)

    total_preguntas_info = Clientes.obtener_total_preguntas()

    if 'error' in total_preguntas_info:
        print(f"Error al obtener el total de preguntas: {total_preguntas_info['error']}")
        return datos

    total_preguntas = total_preguntas_info.get('total', 0)
    print(f"Total de preguntas esperadas: {total_preguntas}")

    if total_preguntas == 0:
        print("Total de preguntas inválido, abortando extracción")
        return datos

    respuestas = AlmacenModel.objects.all().order_by('id_usuario', 'no_pregunta')

    for r in respuestas:
        respuestas_por_usuario[r.id_usuario].append(r.id_respuesta)

    for usuario_id, respuestas_usuario in respuestas_por_usuario.items():
        if len(respuestas_usuario) < total_preguntas:
            respuestas_usuario.extend([0] * (total_preguntas - len(respuestas_usuario)))
        elif len(respuestas_usuario) > total_preguntas:
            respuestas_usuario = respuestas_usuario[:total_preguntas]

        datos.append(respuestas_usuario)

    print(f"Total de usuarios procesados: {len(datos)}")
    return datos

#    print("Datos obtenidos para clustering:", datos)
 #   return datos

