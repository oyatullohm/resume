
# digital VMjqg2&97YK9zXz

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import environ
env = environ.Env()
env.read_env()
# from .local_settings import SECRET_KEY

SECRET_KEY = env.str('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = [ 'my.activeresume.uz','127.0.0.1']


SITE_ID = 1
INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.staticfiles',
    'main',
    'rosetta',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",

]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join( BASE_DIR / 'template')],
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

ALLOW_PARALLEL_RUNS = True
SOCIALACCOUNT_LOGIN_ON_GET=True




AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',

)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False


WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# import dj_database_url
DATABASES = {
    'default': #dj_database_url.parse(env.str('DATABASE_URL'))
        {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
gettext = lambda s:s

LANGUAGE_CODE = 'uz'
LANGUAGES = (
    ('en',gettext("English")),
    ('uz',gettext("Uzbek")),
('ru',gettext("Russian")),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)



STATIC_ROOT = os.path.join(BASE_DIR  / "static")
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#      os.path.join(BASE_DIR / "staticfiles"),
# )

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR , "media")
# STATIC_URL = 'static/'
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME =env.str('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL =env.str('AWS_DEFAULT_ACL')
AWS_S3_ENDPOINT_URL =env.str('AWS_S3_ENDPOINT_URL')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}


AWS_MEDIA_LOCATION = 'media'
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'portfolio.cloud_.MediaStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'main.CustomUser'


# Bottom of the file

EMAIL_BACKEND= env.str('EMAIL_BACKEND')
EMAIL_HOST          = env.str('EMAIL_HOST')
DEFAULT_FROM_EMAIL  = env.str('DEFAULT_FROM_EMAIL')
EMAIL_HOST_USER     = env.str('EMAIL_HOST_USER')
SERVER_EMAIL        = env.str('SERVER_EMAIL')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
EMAIL_PORT          = env.int('EMAIL_PORT')
EMAIL_USE_TLS       = True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# LOGGING = {
#     'version':1,
#     'handlers':{
#          'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log'
#         },
#         'console':{'class':'logging.StreamHandler'}
#     },
#     'loggers':{
#         'django.db.backends':{
#             'handlers':['console','file'],
#             'level':'DEBUG'
#                     }
#                }
# }
