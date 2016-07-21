from django.conf.urls import *
from .views import *

urlpatterns = patterns('ficha_granos_basicos.views',
    url(r'^$', 'consulta', name='index-granos-basicos'),
    url(r'^genero-y-produccion/$', 'genero_produccion', name='genero-y-produccion'),
    url(r'^composicion-familiar/$', 'composicion_familiar', name='composicion-familiar'),
    url(r'^georeferencia/$', 'georeferencia', name='georeferencia'),
    url(r'^caracteristicas-parcela/$', 'caracteristicas_parcela', name='caracteristicas-parcela'),

    url(r'^ajax/comunies/$', 'get_comunies', name='get-comunies'),
)
