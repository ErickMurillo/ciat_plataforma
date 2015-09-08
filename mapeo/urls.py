from django.conf.urls import *
from .views import *

urlpatterns = patterns('mapeo.views',
    url(r'^$', 'indexview', name='index-mapeo'),
    url(r'^proyectos/$', 'proyectos', name='proyectos'),

)
