from django.conf.urls import *
from django.views.generic import ListView, DetailView
from models import Notas
from .views import HomeView

urlpatterns = patterns('notas.views',
    url(r'^$', 'lista_notas', name="notas_list"),
    url(r'^pais/(?P<id>\d+)/$', 'lista_notas_pais', name="notas_list"),
    url(r'^ver/(?P<id>\d+)/$', 'comentar_nota', name='comentar-nota'),
    url(r'^(?P<id>\d+)/$', 'detalle_notas', name='detalle-notas'),
    url(r'^crear/$', 'crear_nota', name="crear-nota"),
    url(r'^editar/(?P<id>\d+)/$', 'editar_nota', name='editar-nota'),
    url(r'^borrar/(?P<id>\d+)/$', 'borrar_nota', name='borrar-nota'),
    url(r'^nuevobase/$', HomeView.as_view()),
    )