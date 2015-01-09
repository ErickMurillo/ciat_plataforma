#import os
from django.conf.urls import *
from django.conf import settings
from django.views.generic import TemplateView
from .views import HomePageView

urlpatterns = patterns('monitoreo.monitoreo.views',
    url(r'^$', HomePageView.as_view(), name='home'),
    #(r'^$', 'index'),
    (r'^index/$', 'inicio'),
    (r'^ajax/organi/$', 'get_organi'),
    (r'^ajax/munis/$', 'get_munis'),
    (r'^ajax/comunies/$', 'get_comunies'),
    #viejas urls
    (r'^index/ajax/organizaciones/(?P<departamento>\d+)/$', 'get_organizacion'),
    (r'^index/ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    (r'^index/ajax/comunidad/(?P<municipio>\d+)/$', 'get_comunidad'),
    #graficas para los indicadores
    (r'^grafo/organizacion/(?P<tipo>\w+)/$', 'organizacion_grafos'),
    (r'^grafo/agua-disponibilidad/(?P<tipo>\d+)/$', 'agua_grafos_disponibilidad'),
    (r'^grafo/fincas/(?P<tipo>\w+)/$', 'fincas_grafos'),
    (r'^grafo/arboles/(?P<tipo>\w+)/$', 'arboles_grafos'),
    (r'^grafo/manejosuelo/(?P<tipo>\w+)/$', 'grafo_manejosuelo'),
    (r'^grafo/ingreso/(?P<tipo>\w+)/$', 'grafos_ingreso'),
    (r'^grafo/bienes/(?P<tipo>\w+)/$', 'grafos_bienes'),
    (r'^grafo/ahorro-credito/(?P<tipo>\w+)/$', 'ahorro_credito_grafos'),
    (r'^mapa/$', 'obtener_lista'),
    (r'^ayuda/$',  TemplateView.as_view(template_name="monitoreo/acerca.html")),
    (r'^exportar/(?P<modela>\d+)/$', 'spss_xls'),
    (r'^(?P<vista>\w+)/$', '_get_view'),
    
)
