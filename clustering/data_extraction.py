from almacen_app.models import DatosGeneralesModel, RespuestaModel
from clients.clients import Clientes

def obtener_datos_usuarios():
    datos = []
    usuarios = DatosGeneralesModel.objects.all()
    respuestas = RespuestaModel.objects.all()


    preguntas = Clientes.obtener_total_preguntas()
    for usuario in usuarios:
        respuestas_usuario = respuestas.filter(id_usuario=usuario.user.id)
        respuestas_numericas = [r.id_respuesta for r in respuestas_usuario]

        if len(respuestas_numericas) < preguntas['total']:
            print(f"Usuario {usuario.id} tiene {len(respuestas_numericas)} respuestas, rellenando con ceros.")
            respuestas_numericas.extend([0] * (preguntas['total'] - len(respuestas_numericas)))  # Rellenar con ceros
        
        datos.append(respuestas_numericas)

    print("Datos obtenidos para clustering:", datos)
    return datos
