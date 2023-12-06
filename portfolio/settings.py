
# digital VMjqg2&97YK9zXz

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# from .local_settings import SECRET_KEY

SECRET_KEY = 'django-insecure-&y+=*pym#n0fgg7*i$ytfg3lvh+%$2opa&8or*tv6b0swaqx$w'

DEBUG = False
# DEBUG =  True


ALLOWED_HOSTS = ['www.my.activeresume.uz','my.activeresume.uz','127.0.0.1']


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
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True





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
# MEDIA_ROOT = '/media/'

STATICFILES_DIRS = (
     os.path.join(BASE_DIR / "staticfiles"),
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR , "media")



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'main.CustomUser'


# Bottom of the file

EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST          = 'smtp.yandex.ru'
DEFAULT_FROM_EMAIL  = 'oyatulloh1988@yandex.com'
EMAIL_HOST_USER     = 'oyatulloh1988@yandex.com'
SERVER_EMAIL        = 'oyatulloh1988@yandex.com'
EMAIL_HOST_PASSWORD = 'Aa@9005233'
EMAIL_PORT          = 587
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
