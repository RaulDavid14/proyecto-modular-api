from django.conf import settings
import requests


class Clientes():
    
    @staticmethod
    def obtener_total_preguntas():
        url = f"{settings.APIS['cfca_url']}/total-preguntas"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f'No se pudo obtener el total de preguntas') 
            return None
    
    @staticmethod
    def get_cuestionarios():
        url = f"{settings.APIS['cfca_url']}/cuestionarios/all/"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None 
        