"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8@**@&-7p&ge-^ss#^c=(mwgbgvvvfxqi!m-j#vqy!rab2q=yy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# The following (INSTALLED_APPS) holds the names of all Django applications that are activated in this Django instance.
# Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects.

INSTALLED_APPS = (
    'django.contrib.admin',  # admin site
    'django.contrib.auth',  # authentication system
    'django.contrib.contenttypes',  # framework for content types
    'django.contrib.sessions',  # session framework
    'django.contrib.messages',  # messaging framework
    'django.contrib.staticfiles',  # framework for managing static files
    'polls',  # use the 'polls' app
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS is a list of filesystem directories to check when loading Django templates; it's a search path.
        # [os.path.join(BASE_DIR, 'templates') => concatenates folder paths, giving ".../mysite/templates/"
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # If DIRS is empty, but APP_DIRS is set to 'True', Django automatically looks for a templates/
        # subdirectory within each application package, for use as a fallback
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# ENGINE: the database to use, e.g.:
# 'django.db.backends.sqlite3', 'django.db.backends.postgresql_psycopg2',
# 'django.db.backends.mysql', or 'django.db.backends.oracle'.

# NAME: the name of the database to use
# The following: os.path.join(BASE_DIR, 'db.sqlite3') stores the database in the project directory

# If you are not using SQLite as your database, additional settings such as USER, PASSWORD, HOST must be added.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# used to be no, now it's nb
LANGUAGE_CODE = 'nb'

# Original value: TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
