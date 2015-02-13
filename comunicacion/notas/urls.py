from django.conf.urls import *

urlpatterns = patterns('comunicacion.notas.views',
    url(r'^$', 'index'),
    url(r'^index-filtrado/(?P<pais_id>\d+)/$', 'index_filtrado', name='filtrar-index'),
    url(r'^notas/$', 'lista_notas', name="notas_list"),
    url(r'^notas-contraparte/(?P<id>\d+)/$', 'lista_notas_contraparte', name="notas_list_contraparte"),
    url(r'^pais/(?P<id>\d+)/$', 'lista_notas_pais', name="notas-list-pais"),
    url(r'^ver/(?P<id>\d+)/$', 'comentar_nota', name='comentar-nota'),
    url(r'^(?P<id>\d+)/$', 'detalle_notas', name='detalle-notas'),
    url(r'^crear/$', 'crear_nota', name="crear-nota"),
    url(r'^editar/(?P<id>\d+)/$', 'editar_nota', name='editar-nota'),
    url(r'^borrar/(?P<id>\d+)/$', 'borrar_nota', name='borrar-nota'),

    )