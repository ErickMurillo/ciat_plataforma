from django.conf.urls import *
from .views import *

urlpatterns = patterns('guias_cacao.views',
    url(r'^$', 'index_ficha_sombra', name='index-cacao'),
    url(r'^riqueza/$', 'riqueza_sombra', name='riqueza-cacao'),
    url(r'^analisis/$', 'analisis_sombra', name='analisis-cacao'),
    url(r'^cobertura/$', 'cobertura_sombra', name='cobertura-cacao'),
    url(r'^api/productor/$', 'get_productor', name='productor-cacao'),

)
