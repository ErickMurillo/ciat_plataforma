"""
Django settings for ciat_plaforma project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from local_settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xz^@^p+q0mku0dpdb&046qt6e4r=*zkxh0er(5l*x5u3x3kq+@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    #apps para mejorar el admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps solo de comunicion
    'comunicacion.aliados',
    'comunicacion.contrapartes',
    'comunicacion.foros',
    'comunicacion.agendas',
    'comunicacion.notas',
    'comunicacion.lugar',
    #apps solo de analisis
    'analisis.analisis',
    'analisis.configuracion',
    #apps solo de monitoreo,
    #apps de terceros
    'smart_selects',
    'sorl.thumbnail',
    'ckeditor',
    'magicembed',
    'tagging',
    'tagging_autocomplete',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ciat_plaforma.urls'

WSGI_APPLICATION = 'ciat_plaforma.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-ni'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'static_media/media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_media"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    
    )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

AUTH_PROFILE_MODULE = 'comunicacion.contrapartes.UserProfile'

LOGIN_REDIRECT_URL = '/foros/perfil'

CKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'

CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'static_media/uploads/')

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': 630,
    },
}

CKEDITOR_JQUERY_URL = 'https://code.jquery.com/jquery-2.1.3.min.js'
