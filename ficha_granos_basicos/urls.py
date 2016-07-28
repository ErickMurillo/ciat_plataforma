from django.conf.urls import *
from .views import *

urlpatterns = patterns('ficha_granos_basicos.views',
    url(r'^$', 'consulta', name='index-granos-basicos'),
    url(r'^genero-y-produccion/$', 'genero_produccion', name='genero-y-produccion'),
    url(r'^composicion-familiar/$', 'composicion_familiar', name='composicion-familiar'),
    url(r'^georeferencia/$', 'georeferencia', name='georeferencia'),
    url(r'^caracteristicas-parcela/$', 'caracteristicas_parcela', name='caracteristicas-parcela'),
    url(r'^ciclo-productivo/$', 'ciclo_productivo', name='ciclo-productivo'),
    url(r'^uso-suelo/$', 'uso_suelo', name='uso-suelo'),
    url(r'^recursos-economicos/$', 'recursos_economicos', name='recursos-economicos'),

    url(r'^ajax/comunies/$', 'get_comunies', name='get-comunies'),
)
