# -*- coding: UTF-8 -*-

from django import forms
from django.forms import ModelForm
from .models import *
from analisis.configuracion.models import SitioAccion, AreaAccion, Plataforma

class MapeoConsulta(forms.Form):
    area_accion = forms.ModelChoiceField(queryset=AreaAccion.objects.order_by('nombre'),
                                  required=False,
                                  label=u'Area de acción')
    sitio_accion = forms.ModelChoiceField(queryset=SitioAccion.objects.order_by('nombre')
                                , required=False,
                                label=u'Sitio de acción')
    alianza = forms.ModelChoiceField(queryset=Plataforma.objects.exclude(id=8).order_by('nombre'), required=False, label=u'Plataforma')
    #proyectos = forms.ModelChoiceField(queryset=Proyectos.objects.order_by('nombre'),
    #                              required=False,
    #                              label=u'Proyectos')
