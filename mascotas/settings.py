AUTH_USER_MODEL = 'mascotas.Usuario'
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'tu_clave_secreta_generada_aleatoriamente'

DEBUG = True

ALLOWED_HOSTS = []

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mascotas.apps.MascotasConfig',  # Reemplaza 'Adoptame' con el nombre real de tu aplicación
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs
ROOT_URLCONF = 'mascotas.urls'  # Reemplaza 'Adoptame' con el nombre real de tu aplicación

# Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mascotas', 'templates')],  # Ajusta la ruta según la estructura de tu proyecto
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de la base de datos (puedes cambiar a tu preferencia, por ejemplo, usar PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Configuración de archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Zona horaria y configuración internacional
TIME_ZONE = 'UTC'
USE_TZ = True
LANGUAGE_CODE = 'es'
USE_I18N = True
USE_L10N = True
