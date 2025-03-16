from .base import *

DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_produccion['database'],
        'USER': db_produccion['user'],
        'PASSWORD': db_produccion['password'],
        'HOST': db_produccion['host'],  
        'PORT': db_produccion['port'],  
    },
}
