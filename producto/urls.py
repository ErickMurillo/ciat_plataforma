from django.conf.urls import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^pablo/$', TemplateView.as_view(template_name="producto/index.html"),

    )