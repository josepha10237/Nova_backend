from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-pp7yklklgp!7y$h%$o%#xq5%9lo(2ni&4to8^guu&n-%^xl*d*')

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'False'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'corsheaders',
    'storages',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Nova1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Nova1.wsgi.application'

# Database Neon
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_D2fqihz4JxOQ@ep-lingering-voice-ay6v6wa8-pooler.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require',
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static & Media (Cloudinary + Whitenoise)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'

# 1. Configuration du stockage par défaut avec django-storages (S3)
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# 2. Tes identifiants S3 Supabase
AWS_ACCESS_KEY_ID = 'c347fa829aa283eb1fc4ef67bca65fc5'
AWS_SECRET_ACCESS_KEY = '15049365da853f7ba86f4e03f49da8b45d51bd75e69784ef5911e2e5b59b21ea'
AWS_STORAGE_BUCKET_NAME = 'NOVA'
AWS_S3_ENDPOINT_URL = 'https://ayvkiiqmxqtfnifqyjlo.supabase.co/storage/v1/s3'  # Corrigé (sans le double storage)
AWS_S3_REGION_NAME = 'eu-west-1'  # Mets la région exacte indiquée sur ton dashboard Supabase si ce n'est pas us-east-1
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    'https://*.up.railway.app',
    'https://nova-pour-tous1.netlify.app',
]