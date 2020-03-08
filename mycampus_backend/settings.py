"""
Django settings for mycampus_backend project.
Generated by 'django-admin startproject' using Django 3.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["TEST_DATABASE_URL"] = "postgres://ojhdhrbhpgmdql:fbba896cd6b4762ef7cbf3393890a9fffd0e9487983c70899cb7421f34a00e3c@ec2-3-234-109-123.compute-1.amazonaws.com:5432/dfg7hq6lpj21id"

#Login and logout links to redirect! 
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG == True:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '(f6+e*ezkjs_-212*_ryvooh$*a$5%+l9$&g^1&z!oydq^sm-2'
else:
    SECRET_KEY = os.environ['SECRET_KEY']


ALLOWED_HOSTS = []

HASHID_FIELD_SALT = "hahahah" #magic salt
# Application definition

INSTALLED_APPS = [
    'users',
    'events',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'behave_django',
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

ROOT_URLCONF = 'mycampus_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mycampus_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# Postgres Database from mycampus-backend created with heroku.

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3'
        }
        
    }
else:
    DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'dac009epqo9i2t',
        'USER':'chpiszhwmbnnpp',
        'PASSWORD':'29c18fe4a75795f662225381e1898c6e0a5e75450e1707904522821eb0e9acd8',
        'HOST':'ec2-52-203-98-126.compute-1.amazonaws.com',
        'POST':'5432',
        'ATOMATIC_REQUESTS':True,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

NOSE_ARGS = ['--nocapture',
             '--nologcapture',]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# Activate Django-Heroku.
# Configure Django App for Heroku.
django_heroku.settings(locals(), test_runner=False)