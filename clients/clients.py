from django.conf import settings
import requests


class Clientes():
    
    @staticmethod
    def obtener_total_preguntas():
        url = f'{settings.APIS['cfca_url']}total-preguntas'
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else: 
            return {'error': 'No se pudo obtener el total de preguntas', 'status' : response.status_code}