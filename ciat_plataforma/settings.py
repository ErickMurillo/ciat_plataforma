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




# Application definition

INSTALLED_APPS = (
    #apps para mejorar el admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    #apps de terceros
    'smart_selects',
    'sorl.thumbnail',
    'ckeditor',
    'magicembed',
    'tagging',
    'tagging_autocomplete',
    'selectable',
    'south',
    'rosetta',
    'ajax_select',

    'comunicacion.lugar',
    #apps solo de mapeo
    'analisis.configuracion',
    'mapeo',
    #apps solo de analisis
    'analisis.analisis',
    #apps solo de comunicion
    #'comunicacion.aliados',
    'comunicacion.contrapartes',
    'comunicacion.foros',
    'comunicacion.agendas',
    'comunicacion.notas',
    
    #apps solo de monitoreo,
    'monitoreo.monitoreo',
    'monitoreo.indicador01',
    'monitoreo.indicador02',
    'monitoreo.indicador05',
    'monitoreo.indicador06',
    'monitoreo.indicador07',
    'monitoreo.indicador08',
    'monitoreo.indicador09',
    'monitoreo.indicador10',
    'monitoreo.indicador11',
    'monitoreo.indicador12',
    'monitoreo.indicador13',
    'monitoreo.indicador14',
    'monitoreo.indicador15',
    'monitoreo.indicador16',
    'monitoreo.indicador17',
    'monitoreo.indicador18',
    'monitoreo.indicador19',
    'monitoreo.indicador20',
    


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'ciat_plataforma.urls'

WSGI_APPLICATION = 'ciat_plataforma.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-ni'

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
                ('en', _('English')),
                ('es', _('Spanish')),
            )

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

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

CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'static_media/media/')

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': 500,
    },
}

CKEDITOR_JQUERY_URL = 'https://code.jquery.com/jquery-2.1.3.min.js'

NO_DATA_GRAPH_URL = ''

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    )


