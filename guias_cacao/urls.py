from django.conf.urls import *
from .views import *

urlpatterns = patterns('guias_cacao.views',
    url(r'^$', 'index_ficha_sombra', name='index-cacao'),
    url(r'^sombra/riqueza/$', 'riqueza_sombra', name='riqueza-cacao'),
    url(r'^sombra/analisis/$', 'analisis_sombra', name='analisis-cacao'),
    url(r'^sombra/cobertura/$', 'cobertura_sombra', name='cobertura-cacao'),
    url(r'^sombra/densidad/$', 'densidad_sombra', name='densidad-cacao'),
    url(r'^sombra/acciones/$', 'acciones_sombra', name='acciones-cacao'),
    url(r'^sombra/caracterizacion/$', 'caracterizacion_sombra', name='caracterizacion-cacao'),
    url(r'^sombra/dominancia/$', 'dominancia_sombra', name='dominancia-cacao'),
    url(r'^sombra/dimensiones/$', 'dimensiones_sombra', name='dimensiones-cacao'),

    #urls de poda
    url(r'^poda/altura/$', 'altura_poda', name='altura-poda'),
    url(r'^poda/ancho-copa/$', 'ancho_poda', name='ancho-poda'),
    url(r'^poda/produccion/$', 'produccion_poda', name='produccion-poda'),
    url(r'^poda/atributos/$', 'atributos_poda', name='produccion-poda'),
    url(r'^poda/analisis/$', 'analisis_poda', name='analisis-poda'),
    url(r'^poda/tipos-poda/$', 'tipo_poda', name='tipo-poda'),
    url(r'^poda/acciones/$', 'acciones_poda', name='acciones-poda'),

    #urls de plaga
    url(r'^plaga/historial/$', 'historial_plaga', name='historial-plaga'),
    url(r'^plaga/acciones/$', 'acciones_plaga', name='acciones-plaga'),
    url(r'^plaga/fuente-incidencia/$', 'fuente_incidencia_plaga', name='fuente-incidencia-plaga'),

    url(r'^api/productor/$', 'get_productor', name='productor-cacao'),
)
