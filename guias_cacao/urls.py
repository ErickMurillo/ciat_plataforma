from django.conf.urls import *
from .views import *

urlpatterns = patterns('guias_cacao.views',
    url(r'^$', 'index_ficha_sombra', name='index-cacao'),
    url(r'^riqueza/$', 'sombra_riqueza', name='riqueza-cacao'),
    url(r'^api/productor/$', 'get_productor', name='productor-cacao'),

)
