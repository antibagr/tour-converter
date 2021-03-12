import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True  # int(os.getenv("DEBUG", default=0))

ALLOWED_HOSTS = ["*"] if DEBUG else os.getenv("DJANGO_ALLOWED_HOSTS").split(" ")


INSTALLED_APPS = [
    # Current project apps
    'converter.apps.ConverterConfig',

    # third-party installed,
    # 'phonenumber_field',
    # 'crispy_forms',
    # 'sorl.thumbnail',
    # 'widget_tweaks',
    # 'rest_framework',
    # 'graphene_django',
    # "django_filters",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'chat.middleware.ActiveUserMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

ASGI_APPLICATION = 'src.asgi.application'
WSGI_APPLICATION = 'src.wsgi.application'

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [(os.getenv("REDIS_HOST"), os.getenv("REDIS_PORT"))],
#         },
#     },
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("PG_DATABASE"),
        'HOST': os.getenv("PG_HOST"),
        'USER': os.getenv("PG_USER"),
        'PASSWORD': os.getenv("PG_PASSWORD"),
        'PORT': os.getenv("PG_PORT"),
    }
}


# AUTH_USER_MODEL = 'account.User'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
TIME_ZONE = 'Europe/Moscow'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'


MEDIA_ROOT = ROOT_DIR / 'media'
MEDIA_URL = '/media/'

# TEMPLATES_DIR = BASE_DIR / 'templates'

"""

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'pages-home'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hatehatehatehate.everything@gmail.com'
EMAIL_HOST_PASSWORD = 'vydvzohahbfsounc'


# GRAPHQL

# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = 5

# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache
USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7


GRAPHENE = {
    "SCHEMA": "chat.schema.schema",
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ],
    'SCHEMA_OUTPUT': os.path.join(STATIC_ROOT, 'js', 'schema.graphql'),
    'SCHEMA_INDENT': 2,

}
"""
