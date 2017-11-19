"""
Django settings for sixty_mill project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Settings.py for LocalDev 

import os

# settings.py
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# PROJECT_ROOT is the directory for settings.py. sm_config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR is the directory for manage.py. SixtyMill_repo


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Variables
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = False

ALLOWED_HOSTS = ['*']

# Heroku settings

if os.getcwd() == '/app':
    # in development og.getcwd is
    # /Users/macbook/djangoProjects/sixtymill/sixty_mill/sixty_mill

    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost')
     }

     # Honor the 'X-Forwarded-Proto' header for request.is_secure().
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

     # Alow all host headers.
    ALLOWED_HOSTS = ['www.sixtymill.com', 'sixtymill.com', 'fierce-thicket-38238.herokuapp.com']

    DEBUG = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'bootstrap3',
    'storages',

    # My apps
    'splash_page',
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

ROOT_URLCONF = 'sm_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sm_config.wsgi.application'


# Update database configuration with $DATABASE_URL
import dj_database_url

# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# Database Variables
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME, #'sixtymill_db',
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': 5432
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#----------------------------------------------------------
#----------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# The following section will be the static files settings and 
# explain static file definitions and functions.

# Django provides django.contrib.staticfiles to help you manage
# Static files. Detailed info at the link below.
# https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#django-admin-collectstatic

# Collect Static -> Collects the static files into STATIC_ROOT.
    # Runs if STATIC_ROOT is NOT empty.

    # Files are copied if their timestamp is greater than the 
    # timestamp of the file in STATIC_ROOT.

    # The default is to look in all locations defined in 
    # STATICFILES_DIRS and in the 'static' directory of apps
    # specified by the INSTALLED_APPS.

    # The management command of collectstatic calls the 
    # post_process() method of the STATICFILES_STORAGE after 
    # each run and passes a list of paths that have been found 
    # by the management command. It also recieves all command
    # line options of the collectstatic. This is used by the 
    # CachedStaticFilesStorage by default.

    # By default, the files receive permissions from 
    # FILE_UPLOAD_PERMISSIONS
    # The directories receive permissions from 
    # FILE_UPLOAD_DIRECTORY_PERMISSIONS

    # for a full list of options run
    # python manage.py collectstatic --help

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # STATIC_ROOT is the absolute path to the directory 
    # where collectstatic will put static files for 
    # deployment.
# STATIC_URL = '/static/'
    # STATIC_URL is used when referring to the static files
    # located in STATIC_ROOT. If not "None", this will be used
    # as the base path for asset definitions (the Media class)
# STATICFILES_DIRS = (os.path.join(BASE_DIR,'splash_page/static'),)
# /Users/macbook/djangoProjects/Projects/SixtyMill_Repo/sm_config/static
    # This setting defines the additional locations the staticfiles
    # app will traverse if the FileSystemFinder finder is enabled,
    # for example if you use the collectstatic to findstatic 
    # management command to use the static file serving view. 
    # this should be a set to a list of strings that contain the 
    # full paths to your additional files directories.
    # This can be a tuple of multiple directories.

# Simplifies static file serving.
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
    # The file storage engine to use when collecting static files 
    # with the "collectstatic"  management command. This is for
    # serving static files from a cloud service or CDN.

# AWS Variables

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'splash_page/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE")

#----------------------------------------------------------
#----------------------------------------------------------

# My settings
LOGIN_URL = '/users/login/'

# Settings for django-bootstrap3
BOOTSTRAP3 = {
    'include_jquery': True,
    'jquery_url': '//code.jquery.com/jquery.min.js',
    'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/',
    }

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Email configurations

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 25
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}








