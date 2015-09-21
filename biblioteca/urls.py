from django.conf.urls import *
from .views import IndexView

urlpatterns = patterns('biblioteca.views',
    url(r'^$', IndexView.as_view(), name='index-biblioteca'),
    url(r'^busqueda/$', 'buscador', name="search"),
    url(r'^detalle-documento/(?P<id_libro>\d+)/$', 'detalle_libro', name="detalle-libro")

)
