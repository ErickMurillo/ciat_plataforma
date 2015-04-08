from django.conf.urls import *

urlpatterns = patterns('analisis.analisis.views',
	url(r'^$', 'inicio', name="inicio"),
    url(r'^salidas/$', 'post', name='salidas'),
    )