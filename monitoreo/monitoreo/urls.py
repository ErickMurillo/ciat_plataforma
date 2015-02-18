#import os
from django.conf.urls import *
from django.views.generic import TemplateView
from .views import HomePageView, HomePageViewfail

urlpatterns = patterns('monitoreo.monitoreo.views',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^prueba/$', HomePageViewfail.as_view(), name='prueba'),
    #(r'^$', 'index'),
    url(r'^index/$', 'inicio', name='index'),
    url(r'^ajax/organi/$', 'get_organi', name='get-organi'),
    url(r'^ajax/munis/$', 'get_munis', name='get-munis'),
    url(r'^ajax/comunies/$', 'get_comunies', name='get-comunies'),
    #viejas urls
    url(r'^index/ajax/organizaciones/(?P<departamento>\d+)/$', 
                                    'get_organizacion', name='get-organizacion'),
    url(r'^index/ajax/municipio/(?P<departamento>\d+)/$', 
                                    'get_municipios', name='get=municipios'),
    url(r'^index/ajax/comunidad/(?P<municipio>\d+)/$', 
                                    'get_comunidad', name='get-comunidad'),
    #graficas para los indicadores
    url(r'^grafo/organizacion/(?P<tipo>\w+)/$', 
                                    'organizacion_grafos', name='organizacion-grafos'),
    url(r'^grafo/agua-disponibilidad/(?P<tipo>\d+)/$', 
                                    'agua_grafos_disponibilidad', 
                                    name='agua-grafos-disponibilidad'),
    url(r'^grafo/fincas/(?P<tipo>\w+)/$', 'fincas_grafos', name='fincas-grafos'),
    url(r'^grafo/fincas/entre/(?P<tipo>\w+)/$', 'fincas_grafos_entrevistada', name='fincas-grafos-entre'),
    url(r'^grafo/arboles/(?P<tipo>\w+)/$', 'arboles_grafos', name='arboles-grafos'),
    url(r'^grafo/manejosuelo/(?P<tipo>\w+)/$', 'grafo_manejosuelo', 
                                            name='grafo_manejosuelo'),
    url(r'^grafo/ingreso/(?P<tipo>\w+)/$', 'grafos_ingreso', name='grafos-ingreso'),
    url(r'^grafo/bienes/(?P<tipo>\w+)/$', 'grafos_bienes', name='grafos-bienes'),
    url(r'^grafo/ahorro-credito/(?P<tipo>\w+)/$', 'ahorro_credito_grafos', 
                                            name='ahorro-credito-grafos'),
    url(r'^mapa/$', 'obtener_lista', name='obtener-lista'),
    url(r'^ayuda/$',  TemplateView.as_view(template_name="monitoreo/acerca.html"), 
                        name='ayuda'),
    url(r'^exportar/(?P<modela>\d+)/$', 'spss_xls', name='spss-xls'),
    url(r'^(?P<vista>\w+)/$', '_get_view', name='get-view'),
    
)
