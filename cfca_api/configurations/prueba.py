from .credenciales import *
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

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
