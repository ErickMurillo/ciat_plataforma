from django.conf.urls import *
from .views import IndexView

urlpatterns = patterns('producto.views',
	url(r'^$', IndexView.as_view(), name='index-producto'),

    )