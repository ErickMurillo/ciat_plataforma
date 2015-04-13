from django.conf.urls import *

urlpatterns = patterns('analisis.analisis.views',
	url(r'^$', 'inicio', name="inicio"),
    url(r'^salidas/$', 'post', name='salidas'),
    url(r'^salida1/$', 'salida1', name='salida1'),
    url(r'^salida2/$', 'salida2', name='salida2'),
    url(r'^salida3/$', 'salida3', name='salida3'),
    url(r'^salida4/$', 'salida4', name='salida4'),
    url(r'^salida5/$', 'salida5', name='salida5'),
    url(r'^salida5b/$', 'salida5b', name='salida5b'),
    url(r'^salida6/$', 'salida6', name='salida6'),
    )