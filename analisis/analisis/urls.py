from django.conf.urls import *

from analisis.analisis.views import IndexView

urlpatterns = patterns('analisis.analisis.views',
    url(r'^$', IndexView.as_view()),
    )