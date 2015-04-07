from django.conf.urls import *

from analisis.analisis.views import IndexView

urlpatterns = patterns('analisis.analisis.views',
	url(r'^$', 'inicio', name="inicio"),
    url(r'^salidas/$', IndexView.as_view()),
    )