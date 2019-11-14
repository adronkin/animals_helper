"""
Django settings for animals_helper project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vnswq%#^f0x8gijts%-jg)(o#n)%ji4-^z%gyee7g_wyk&c1)3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# EMAIL_HOST = 'smtp.mail.ru'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = "@mail.ru"
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True

# if DEBUG:
#     # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#     EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#     EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp/emails/')
# else:
#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'mainapp',
    'authapp',
    'adminapp',
    'crispy_forms',
    'social_django',
    'django_extensions',
    'reserveapp',
    'shelteradminapp',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'animals_helper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mainapp.context_processors.get_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'animals_helper.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'NAME': 'animals_helper',
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'USER': 'bigboss',
    #     'PASSWORD': '63387772',
    #     'HOST': 'localhost'
    # }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

SOCIAL_AUTH_URL_NAMESPACE = 'social'

#AUTH_USER_MODEL = 'authapp.models.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.odnoklassniki.OdnoklassnikiOAuth2',
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# LOGIN_URL = '/authapp/login/'

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'
LANGUAGES = (
    ('ru', 'русский'),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

USE_THOUSAND_SEPARATOR = True

# Подтверждение почты
DOMAIN_NAME = 'http://127.0.0.1:8000'

EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'django@animals_helper.local'
EMAIL_HOST_PASSWORD = 'geekbrains'
EMAIL_USE_SSL = False

# вариант python -m smtpd -n -c DebuggingServer localhost:25
# EMAIL_HOST_USER, EMAIL_HOST_PASSWORD = None, None

# вариант логирования сообщений почты в виде файлов вместо отправки
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'

# проверяет совпадения по email при входе через соцсети
# включена чтобы не было множества одинаковых пользователей
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.associate_by_email',
)

# ключи ВК
SOCIAL_AUTH_VK_OAUTH2_KEY = '7163751'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'xoNTlHt58J1pr6UQ5qxa'

# ключи гугла
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '659908000422-u951chquomj00bigaimdd97rbns9e8kf'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '6lGjkUTyWRpzhiwMeVfFEbnx'



# ключи фейсбука
SOCIAL_AUTH_FACEBOOK_KEY = '391147618442915'
SOCIAL_AUTH_FACEBOOK_SECRET = '70f271d25b6553a8cd4857f2f0e80b7c'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# ключи одноклассники
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY = '512000077349'
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET = '78AD1C99110CC6664A6259F2'
SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_PUBLIC_NAME = 'CGCPCGJGDIHBABABA'



