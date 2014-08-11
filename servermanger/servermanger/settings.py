"""
Django settings for servermanger project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u7va0)xflhk@b3c2*3yeq^i76^$-d@@!r3*0ilqfabc4aq)-o('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'servermangerapp',
    'servermangerapp.bootstrap_toolkit',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_DIRS = (
    'D:\django\servermanger\servermangerapp\templates',
    'D:\django\servermanger\servermangerapp\templates\twitter-bootstrap',
    'D:\django\servermanger\servermangerapp\templates\twitter-bootstrap\bootstrap',
     os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),
    os.path.join('templates'),
)
ROOT_URLCONF = 'servermanger.urls'

WSGI_APPLICATION = 'servermanger.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
 #       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  #  }
'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'servermanger',
        'USER':'root',
        'PASSWORD':'abc123?',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
MEDIA_ROOT = "D:/django/fileupload"
STATIC_URL = '/static/'
STATICFILES_DIRS = (

    os.path.join(os.path.dirname(__file__), '..', 'static').replace('\\','/'),

    os.path.join('static'),
)
