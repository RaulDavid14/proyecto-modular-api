from .credenciales import *
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

APIS = {
    'cfca_url' : 'http://127.0.0.1:8000/api'
    ,'timeout' : 10
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_prueba['database'],
        'USER': db_prueba['user'],
        'PASSWORD': db_prueba['password'],
        'HOST': db_prueba['host'],  
        'PORT': db_prueba['port'],  
    },
}
