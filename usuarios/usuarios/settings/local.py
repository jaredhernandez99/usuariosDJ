from .base import *
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': getSecret('DB_NAME'),
            'USER': getSecret('USER'),
            'PASSWORD': getSecret('PASSWORD'),
            'HOST': 'localhost',
            'PORT': '5432',
    }
}
STATIC_URL = '/static/'
STATICFILES_DIR = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')