from cuestionario.models import RespuestaModel
from catalogos.models import DatosGenerales
from cuestionario.models import PreguntaModel
from clustering.models import  ModeloClustering, DatosClustering

def obtener_datos_usuarios(modelo_nombre="Modelo Predeterminado"):
    # Obtener o crear el modelo de clustering
    modelo, _ = ModeloClustering.objects.get_or_create(
        nombre=modelo_nombre,
        defaults={'num_clusters': 4, 'random_state': 42}
    )
    
    datos = []
    usuarios = DatosGenerales.objects.all()
    respuestas = RespuestaModel.objects.all()

    # Obtener todas las preguntas dinámicamente ordenadas por no_pregunta
    preguntas = PreguntaModel.objects.all().order_by('no_pregunta')
    num_preguntas = len(preguntas)
    print(f"Total de preguntas disponibles: {num_preguntas}")

    respuestas_por_usuario = []
    
    for usuario in usuarios:
        respuestas_usuario = respuestas.filter(id_usuario=usuario.user.id).order_by('no_pregunta')
        respuestas_numericas = [r.id_respuesta for r in respuestas_usuario]

        # Rellenar con ceros hasta la cantidad de preguntas disponibles
        if len(respuestas_numericas) < num_preguntas:
            print(f"Usuario {usuario.id} tiene {len(respuestas_numericas)} respuestas, rellenando con ceros.")
            respuestas_numericas.extend([0] * (num_preguntas - len(respuestas_numericas)))
        
        datos.append(respuestas_numericas)
        respuestas_por_usuario.append({
            'usuario_id': usuario.id,
            'respuestas': respuestas_numericas
        })

    # Guardar los datos originales en el modelo
    DatosClustering.objects.create(
        modelo=modelo,
        datos_originales=respuestas_por_usuario,
        datos_preprocesados=[],
        scaler_utilizado='No aplicado'
    )

    print("Datos obtenidos para clustering:", datos)
    return datos, modelo