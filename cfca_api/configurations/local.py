from .base import *

DEBUG = True

ALLOWED_HOSTS = []


APIS = {
    'cfca_url' : 'http://127.0.0.1:8000/api'
    ,'timeout' : 10
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
