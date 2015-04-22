from django.conf.urls import *

urlpatterns = patterns('analisis.analisis.views',
	url(r'^$', 'inicio', name="inicio"),
    url(r'^salidas/$', 'post', name='salidas'),
    url(r'^salida1/$', 'salida1', name='salida1'),
    url(r'^salida2/$', 'salida2', name='salida2'),
    url(r'^salida3/$', 'salida3', name='salida3'),
    url(r'^salida4/$', 'salida4', name='salida4'),
    )