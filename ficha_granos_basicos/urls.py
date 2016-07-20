from django.conf.urls import *
from .views import *

urlpatterns = patterns('ficha_granos_basicos.views',
    url(r'^$', 'consulta', name='index-granos-basicos'),

)
